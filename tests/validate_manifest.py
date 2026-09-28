"""Validate the deliberately small JSON-subset-of-YAML manifest with stdlib only."""

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RUNTIMES = {"hermes", "omp", "codex"}
TYPES = {"skill", "instruction", "template"}
STATUSES = {"reviewed", "optional", "manual"}
NAME = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*\Z")


def relative_path(value):
    assert isinstance(value, str) and value, f"empty path: {value!r}"
    path = Path(value)
    assert not path.is_absolute() and "\\" not in value and ":" not in value, f"not portable: {value}"
    assert all(part not in {".", "..", ""} for part in value.split("/")), f"path traversal: {value}"
    return path


def validate():
    manifest = json.loads((ROOT / "manifest.yaml").read_text(encoding="utf-8"))
    assert manifest["name"] == "agent-stack" and manifest["version"] == 1
    assert re.fullmatch(r"[0-9a-f]{40}", manifest["jev"]["commit"])
    assert manifest["jev"]["commit"] == "08473a5496864e8c97ee6f8f58980131ae16aed2"
    assert manifest["jev"]["mode"] == "external-mcp"
    items = manifest["components"]
    assert isinstance(items, list) and items
    names = set()
    covered = set()
    destinations = set()
    for item in items:
        name = item["name"]
        assert NAME.fullmatch(name) and name not in names, f"duplicate/invalid component: {name}"
        names.add(name)
        assert item["type"] in TYPES and item["status"] in STATUSES
        runtime = item["runtime"]
        assert runtime == "shared" or runtime in RUNTIMES
        source = relative_path(item["source"])
        assert source.parts[0] == ("shared" if runtime == "shared" else "runtimes")
        if runtime != "shared":
            assert source.parts[1] == runtime
        current = ROOT
        for part in source.parts:
            current = current / part
            assert not current.is_symlink(), f"source symlink: {source}"
        assert current.exists() and current.resolve().is_relative_to(ROOT.resolve()), f"missing source: {source}"
        if item["type"] == "skill":
            assert current.is_dir() and (current / "SKILL.md").is_file(), f"invalid skill: {source}"
            text = (current / "SKILL.md").read_text(encoding="utf-8")
            assert text.startswith("---\n") and "\n---\n" in text[4:], f"skill frontmatter: {source}"
            frontmatter = text[4:].split("\n---\n", 1)[0]
            assert re.search(r"(?m)^name:\s*" + re.escape(name) + r"\s*$", frontmatter)
            assert re.search(r"(?m)^description:\s*\S+", frontmatter)
            for reference in re.findall(r"`(references/[^` ]+\.md)`", text):
                assert (current / relative_path(reference)).is_file(), f"missing {reference} in {name}"
        else:
            assert current.is_file(), f"not a file: {source}"
        targets = item["targets"]
        assert isinstance(targets, dict) and targets and set(targets) <= RUNTIMES
        if runtime != "shared":
            assert set(targets) == {runtime}, f"runtime-specific source escapes {runtime}: {name}"
        for target_runtime, target in targets.items():
            parts = relative_path(target).parts
            assert parts[0] in {"skills", "agent-stack"} and len(parts) > 1, f"unsafe target: {target}"
            if item["type"] == "skill":
                assert parts == ("skills", name), f"skill destination: {target}"
            destination = (target_runtime, target.casefold())
            assert destination not in destinations, f"target collision: {target_runtime}/{target}"
            destinations.add(destination)
            covered.add(target_runtime)
        assert isinstance(item["dependencies"], list) and all(isinstance(x, str) for x in item["dependencies"])
        assert isinstance(item["tested_on"], list) and set(item["tested_on"]) <= RUNTIMES
        assert isinstance(item["compatibility"], str) and item["compatibility"].strip()
    assert covered == RUNTIMES, f"missing runtime: {RUNTIMES - covered}"
    for item in items:
        assert all(dependency in names and dependency != item["name"] for dependency in item["dependencies"])
    return len(items)


if __name__ == "__main__":
    print(f"manifest and portable skill structure: OK ({validate()} components)")
