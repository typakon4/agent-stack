"""Isolated installer checks; all writes stay inside temporary runtime homes."""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ENGINE = Path(__file__).resolve().parents[1] / "installers" / "install.py"
SHELL = ENGINE.with_suffix(".sh")


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / "portable"
        (self.repo / "installers").mkdir(parents=True)
        shutil.copy2(ENGINE, self.repo / "installers" / "install.py")
        self.runtime = self.base / "runtime"
        self.runtime.mkdir()
        (self.repo / "shared" / "skills" / "example").mkdir(parents=True)
        (self.repo / "shared" / "skills" / "example" / "SKILL.md").write_text("new skill\n")
        (self.repo / "shared" / "templates").mkdir(parents=True)
        (self.repo / "shared" / "templates" / "optional.md").write_text("optional\n")
        self.items = [
            {"name": "example", "type": "skill", "source": "shared/skills/example", "targets": {"hermes": "skills/example", "omp": "skills/example", "codex": "skills/example"}, "status": "reviewed"},
            {"name": "optional", "type": "template", "source": "shared/templates/optional.md", "targets": {"hermes": "agent-stack/optional.md"}, "status": "optional"},
            {"name": "manual", "type": "template", "source": "shared/templates/optional.md", "targets": {"hermes": "agent-stack/manual.md"}, "status": "manual"},
        ]
        self.save_manifest()

    def save_manifest(self):
        (self.repo / "manifest.yaml").write_text(json.dumps({"name": "agent-stack", "version": 1, "components": self.items}))

    def run_install(self, *args, wrapper=False):
        command = [sys.executable, str(self.repo / "installers" / "install.py")]
        if wrapper:
            shutil.copy2(SHELL, self.repo / "installers" / "install.sh")
            command = ["sh", str(self.repo / "installers" / "install.sh")]
        return subprocess.run([*command, *args], text=True, capture_output=True)

    def test_preview_and_selective_replacement(self):
        preview = self.run_install("hermes")
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn("DRY-RUN example", preview.stdout)
        self.assertNotIn("optional", preview.stdout)
        self.assertFalse((self.runtime / "skills").exists())
        explicit = self.run_install("hermes", "--dry-run", "--component", "optional", wrapper=os.name != "nt" and shutil.which("sh") is not None)
        self.assertEqual(explicit.returncode, 0, explicit.stderr)
        self.assertIn("DRY-RUN optional", explicit.stdout)
        self.assertFalse((self.runtime / "agent-stack").exists())

        target = self.runtime / "skills" / "example"
        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("previous local skill\n")
        result = self.run_install("hermes", "--apply", "--component", "example", "--component", "optional", "--destination", str(self.runtime))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((target / "SKILL.md").read_text(), "new skill\n")
        self.assertEqual((self.runtime / "agent-stack" / "optional.md").read_text(), "optional\n")
        backups = list((self.runtime / ".agent-stack-backups").glob("skills--example--*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / "SKILL.md").read_text(), "previous local skill\n")

    def test_powershell_wrapper_preview(self):
        powershell = shutil.which("pwsh") or shutil.which("powershell")
        if not powershell:
            self.skipTest("PowerShell is unavailable")
        wrapper = self.repo / "installers" / "install.ps1"
        shutil.copy2(ENGINE.with_suffix(".ps1"), wrapper)
        result = subprocess.run([powershell, "-NoProfile", "-File", str(wrapper), "codex", "--dry-run"], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("DRY-RUN example", result.stdout)
        self.assertFalse((self.runtime / "skills").exists())

    def test_refusals_and_secret_source(self):
        self.assertNotEqual(self.run_install("hermes", "--apply", "--component", "example").returncode, 0)
        self.assertNotEqual(self.run_install("hermes", "--apply", "--destination", str(self.runtime)).returncode, 0)
        for destination in (str(self.repo), str(self.base / "absent"), "relative"):
            with self.subTest(destination=destination):
                self.assertNotEqual(self.run_install("hermes", "--apply", "--component", "example", "--destination", destination).returncode, 0)
        self.assertNotEqual(self.run_install("hermes", "--apply", "--component", "manual", "--destination", str(self.runtime)).returncode, 0)
        self.items[0]["targets"]["hermes"] = "skills/../stolen"
        self.save_manifest()
        self.assertNotEqual(self.run_install("hermes", "--apply", "--component", "example", "--destination", str(self.runtime)).returncode, 0)
        self.items[0]["targets"]["hermes"] = "skills/example"
        (self.repo / "shared" / "skills" / "example" / ".env.production").write_text("secret\n")
        self.save_manifest()
        self.assertNotEqual(self.run_install("hermes", "--apply", "--component", "example", "--destination", str(self.runtime)).returncode, 0)
        self.assertFalse((self.runtime / "skills").exists())

    def test_symlink_destination_refused(self):
        outside = self.base / "outside"
        outside.mkdir()
        try:
            (self.runtime / "skills").symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("creating symlinks is unavailable")
        result = self.run_install("hermes", "--apply", "--component", "example", "--destination", str(self.runtime))
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((outside / "example").exists())


if __name__ == "__main__":
    unittest.main()
