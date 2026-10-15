"""Real manifest/install boundary checks using disposable runtime homes."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[2]
LOCK = json.loads((REPO / "design/source-lock.json").read_text(encoding="utf-8"))
MANIFEST = json.loads((REPO / "manifest.yaml").read_text(encoding="utf-8"))
SKILLS = [*LOCK["skills"], {"name": "design-reference-loop", **LOCK["reference_loop"]}]
ENGINE = REPO / "installers/install.py"


class DesignIntegration(unittest.TestCase):
    def test_exact_reviewed_sources_and_static_surface(self):
        self.assertEqual(len(LOCK["skills"]), 29)
        self.assertEqual(sum(len(s["files"]) for s in LOCK["skills"]), 85)
        for skill in SKILLS:
            root = REPO / skill["path"]
            files = {p.relative_to(root).as_posix(): p for p in root.rglob("*") if p.is_file()}
            self.assertEqual(set(files), set(skill["files"]), skill["name"])
            for name, path in files.items():
                with self.subTest(skill=skill["name"], file=name):
                    self.assertFalse(path.is_symlink())
                    self.assertTrue(name == "LICENSE" or path.suffix == ".md" or name == "agents/openai.yaml")
                    self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), skill["files"][name])

    def test_optional_selection_and_runtime_boundaries(self):
        components = {c["name"]: c for c in MANIFEST["components"]}
        for skill in SKILLS:
            component = components[skill["name"]]
            self.assertEqual(component["status"], "optional")
            self.assertEqual(component["source"], skill["path"])
            expected = {"codex"} if skill["name"] != "design-reference-loop" else {"hermes", "omp", "codex"}
            self.assertEqual(set(component["targets"]), expected)
        for runtime in ("hermes", "omp", "codex"):
            result = subprocess.run([sys.executable, str(ENGINE), runtime, "--dry-run"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            for skill in SKILLS:
                self.assertNotIn("DRY-RUN " + skill["name"] + ":", result.stdout)
        for runtime in ("hermes", "omp"):
            rejected = subprocess.run([sys.executable, str(ENGINE), runtime, "--component", "impeccable-design"], capture_output=True, text=True)
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("unknown or unavailable", rejected.stderr)

    def test_full_selected_install_and_preview_in_disposable_homes(self):
        with tempfile.TemporaryDirectory() as temporary:
            for runtime in ("hermes", "omp", "codex"):
                root = Path(temporary) / runtime
                root.mkdir()
                selected = SKILLS if runtime == "codex" else SKILLS[-1:]
                args = [sys.executable, str(ENGINE), runtime, "--destination", str(root), "--no-clobber"]
                for skill in selected:
                    args.extend(["--component", skill["name"]])
                preview = subprocess.run([*args, "--dry-run"], capture_output=True, text=True)
                self.assertEqual(preview.returncode, 0, preview.stderr)
                self.assertEqual(list(root.iterdir()), [])
                applied = subprocess.run([*args, "--apply"], capture_output=True, text=True)
                self.assertEqual(applied.returncode, 0, applied.stderr)
                expected = {}
                for skill in selected:
                    for name, digest in skill["files"].items():
                        expected[f"skills/{skill['name']}/{name}"] = digest
                actual = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in root.rglob("*") if p.is_file()}
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
