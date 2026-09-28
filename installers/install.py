#!/usr/bin/env python3
"""Preview reviewed components, or install explicitly selected components into a runtime home."""

import argparse
import json
import os
import shutil
import stat
import tempfile
import uuid
from pathlib import Path, PurePosixPath

REPO = Path(__file__).resolve().parents[1]
RUNTIMES = ("hermes", "omp", "codex")
FORBIDDEN = {
    ".git", ".ssh", ".aws", ".env", ".netrc", ".npmrc", "__pycache__",
    "auth.json", "credentials.json", "secrets.json", "tokens.json",
    "cookies.json", "id_ed25519", "id_rsa", "sessions", "session",
    "cache", "logs", "node_modules", "venv", ".venv", "browser_profiles", "state",
}
FORBIDDEN_SUFFIXES = (
    ".db", ".db-wal", ".db-shm", ".db-journal", ".sqlite", ".sqlite3", ".sqlite-wal",
    ".sqlite-shm", ".sqlite3-wal", ".sqlite3-shm", ".pem", ".key", ".p12", ".pfx", ".jsonl", ".pyc",
)


def relative_path(raw):
    if not isinstance(raw, str) or not raw or "\\" in raw:
        raise ValueError(f"invalid relative path: {raw!r}")
    path = PurePosixPath(raw)
    if path.is_absolute() or any(part in (".", "..", "") for part in raw.split("/")) or ":" in raw:
        raise ValueError(f"invalid relative path: {raw!r}")
    return Path(*path.parts)


def check_parts(path, root=None):
    """Reject symlinks in an existing path, including its ancestors."""
    for part in (path, *path.parents):
        if part.is_symlink() or (hasattr(part, "is_junction") and part.is_junction()):
            raise ValueError(f"refusing symlink/junction: {part}")
        if root is not None and part == root:
            break


def check_source(path):
    check_parts(path)
    if not path.exists() or not (path.is_file() or path.is_dir()):
        raise ValueError(f"missing source: {path}")
    entries = [path]
    if path.is_dir():
        for base, dirs, files in os.walk(path):
            entries.extend(Path(base) / name for name in dirs + files)
    for entry in entries:
        name = entry.name.lower()
        if entry.is_symlink() or (hasattr(entry, "is_junction") and entry.is_junction()):
            raise ValueError(f"refusing source symlink: {entry}")
        if name in FORBIDDEN or name.startswith((".env", "cookies.")) or name.endswith(FORBIDDEN_SUFFIXES):
            raise ValueError(f"refusing secret/state filename: {entry}")


def destination_root(raw):
    root = Path(raw).expanduser()
    if not root.is_absolute() or not root.is_dir() or root == root.parent:
        raise ValueError("--destination must be an absolute existing runtime home (not a filesystem root)")
    check_parts(root)
    if root.is_relative_to(REPO) or REPO.is_relative_to(root):
        raise ValueError("refusing repository as destination")
    return root


def selected_items(runtime, names):
    manifest = json.loads((REPO / "manifest.yaml").read_text(encoding="utf-8"))
    items = {item["name"]: item for item in manifest["components"]}
    for name in names:
        item = items.get(name)
        if item is None or runtime not in item["targets"]:
            raise ValueError(f"{name}: unknown or unavailable for {runtime}")
        if item["status"] == "manual":
            raise ValueError(f"{name}: manual component cannot be installed")
        if item["status"] not in ("reviewed", "optional"):
            raise ValueError(f"{name}: component is not approved")
        yield item


def plan(runtime, names, root):
    targets = set()
    for item in selected_items(runtime, names):
        source_rel = relative_path(item["source"])
        target_rel = relative_path(item["targets"][runtime])
        # Installation is limited to standalone skills and agent-stack-owned files.
        if source_rel.parts[0] not in ("shared", "runtimes"):
            raise ValueError(f"{item['name']}: source outside portable content")
        if item["type"] == "skill":
            valid = len(target_rel.parts) == 2 and target_rel.parts[0] == "skills"
        else:
            valid = len(target_rel.parts) == 2 and target_rel.parts[0] == "agent-stack"
        if not valid or target_rel.parts[-1].startswith(".") or target_rel.parts[-1].lower() in FORBIDDEN:
            raise ValueError(f"{item['name']}: refusing runtime config/state target")
        if target_rel in targets:
            raise ValueError(f"duplicate destination: {target_rel}")
        targets.add(target_rel)
        source = REPO / source_rel
        check_source(source)
        target = root / target_rel if root else None
        if target:
            check_parts(target, root)
            if target.exists():
                if source.is_dir() != target.is_dir():
                    raise ValueError(f"{item['name']}: existing target has different type")
                if target.is_dir():
                    for base, dirs, files in os.walk(target):
                        for name in dirs + files:
                            check_parts(Path(base) / name, root)
        yield item["name"], source, target_rel, target


def install(source, target, root):
    check_parts(target, root)
    target.parent.mkdir(parents=True, exist_ok=True)
    check_parts(target, root)
    with tempfile.TemporaryDirectory(prefix=".agent-stack-stage-", dir=target.parent) as temporary:
        staged = Path(temporary) / "payload"
        if source.is_dir():
            shutil.copytree(source, staged)
        else:
            shutil.copy2(source, staged)
        backup = None
        if target.exists():
            backups = root / ".agent-stack-backups"
            check_parts(backups, root)
            backups.mkdir(mode=0o700, exist_ok=True)
            if os.name != "nt" and stat.S_IMODE(backups.stat().st_mode) & 0o077:
                raise ValueError(f"backup directory must be owner-only: {backups}")
            backup = backups / f"{target.parent.name}--{target.name}--{uuid.uuid4().hex}"
            os.replace(target, backup)
        try:
            os.replace(staged, target)
        except OSError:
            if backup is not None:
                os.replace(backup, target)
            raise
        return backup


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runtime", choices=RUNTIMES)
    parser.add_argument("--component", action="append", help="Select one component; repeat for multiple")
    parser.add_argument("--destination", help="Absolute path to an existing runtime home")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="Install selected components")
    mode.add_argument("--dry-run", action="store_true", help="Preview only (the default)")
    args = parser.parse_args(argv)
    if args.apply and (not args.component or not args.destination):
        parser.error("--apply requires --component and --destination")
    try:
        root = destination_root(args.destination) if args.destination else None
        manifest = json.loads((REPO / "manifest.yaml").read_text(encoding="utf-8"))
        names = list(dict.fromkeys(args.component)) if args.component else [
            item["name"] for item in manifest["components"]
            if item["status"] == "reviewed" and args.runtime in item["targets"]
        ]
        actions = list(plan(args.runtime, names, root))
        for name, source, target_rel, target in actions:
            print(f"{'APPLY' if args.apply else 'DRY-RUN'} {name}: {source.relative_to(REPO)} -> {target or target_rel}")
            if args.apply:
                backup = install(source, target, root)
                if backup:
                    print(f"  previous version backed up: {backup}")
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
