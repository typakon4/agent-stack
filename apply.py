#!/usr/bin/env python3
"""Install selected reviewed skills only; dry-run unless --apply is explicit."""

import argparse
import filecmp
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent


def source_files(path):
    files = set()
    for base, dirs, names in os.walk(path):
        for name in dirs + names:
            entry = Path(base) / name
            lower = name.lower()
            if entry.is_symlink():
                raise ValueError(f"Refusing symlink: {entry}")
            if lower.startswith(".env") or lower in {"auth.json", "credentials.json", "id_ed25519", "id_rsa", "sessions", "cache", "logs", "node_modules", "venv", ".venv", "browser_profiles"} or lower.endswith((".db", ".db-wal", ".db-shm", ".pem", ".key", ".p12", ".pfx", ".jsonl")):
                raise ValueError(f"Refusing secret/state filename: {entry}")
        files.update((Path(base) / name).relative_to(path) for name in names)
    return files


def changed_files(source, target, files):
    if not target.exists():
        return len(files)
    entries = list(target.rglob("*"))
    if any(p.is_symlink() for p in entries):
        raise ValueError(f"Refusing symlink in target: {target}")
    existing = {p.relative_to(target) for p in entries if p.is_file()}
    return len(files ^ existing) + sum(not filecmp.cmp(source / name, target / name, shallow=False) for name in files & existing)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=("VPS_HERMES", "PC_HERMES", "OMP"), required=True)
    parser.add_argument("--skills-dir", type=Path, required=True, help="Absolute skills directory on this machine/profile")
    parser.add_argument("--skill", action="append", required=True, help="Repeat to select several manifest names; no 'all'")
    parser.add_argument("--apply", action="store_true", help="Perform changes; default is dry-run")
    args = parser.parse_args()
    root = args.skills_dir.expanduser()
    if not root.is_absolute():
        parser.error("--skills-dir must be absolute")
    root = root.resolve()
    if root.name != "skills" or not root.is_relative_to(Path.home().resolve()) or root.is_relative_to((Path.home() / ".hermes/hermes-agent").resolve()) or root.is_relative_to(REPO):
        parser.error("refusing a skills directory outside the user profile or inside source/upstream")
    items = {entry["name"]: entry for entry in yaml.safe_load((REPO / "manifest.yaml").read_text())["components"]}
    for name in dict.fromkeys(args.skill):
        entry = items.get(name)
        if not entry or entry["type"] != "skill" or entry["status"] not in {"reviewed", "optional"} or args.target not in entry["targets"]:
            parser.error(f"{name}: not approved for {args.target}")
        source = (REPO / entry["path"]).resolve()
        if not source.is_relative_to(REPO / "skills") or not (source / "SKILL.md").is_file():
            parser.error(f"{name}: invalid skill source")
        files = source_files(source)
        category = source.parent.name if source.parent != REPO / "skills" and args.target != "OMP" else ""
        target = root / category / name
        if target.is_symlink() or (target.exists() and not target.is_dir()):
            parser.error(f"{name}: target is not a regular skill directory")
        changes = changed_files(source, target, files)
        print(f"{'APPLY' if args.apply else 'DRY-RUN'} {name}: {source} -> {target}; changed files: {changes}")
        if not args.apply or not changes:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".contour-", dir=target.parent) as staging:
            staged = Path(staging) / name
            shutil.copytree(source, staged)
            backup = None
            if target.exists():
                backups = root.parent / "contour-skill-backups"
                if backups.is_symlink():
                    parser.error("backup directory is a symlink")
                backups.mkdir(mode=0o700, exist_ok=True)
                if backups.stat().st_mode & 0o077:
                    parser.error("backup directory must be owner-only")
                stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
                backup = backups / f"{category or 'root'}--{name}--{stamp}"
                os.rename(target, backup)
            try:
                os.rename(staged, target)
            except OSError:
                if backup is not None:
                    os.rename(backup, target)
                raise
            if backup is not None:
                print(f"  previous skill preserved: {backup}")


if __name__ == "__main__":
    main()
