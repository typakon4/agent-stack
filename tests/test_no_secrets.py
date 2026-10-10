"""Cheap committed-file gate, not a guarantee that every secret is detectable."""

from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "installers"))
from safety import forbidden_filename, suspicious_content


class PortableSafety(unittest.TestCase):
    def test_detector_catches_realistic_patterns_without_embedded_keys(self):
        self.assertIn("openai key", suspicious_content(b"sk-" + b"A" * 32))
        self.assertIn("openrouter key", suspicious_content(b"sk-or-v1-" + b"Z" * 36))
        self.assertIn("telegram bot token", suspicious_content(b"123456789:" + b"a" * 35))
        self.assertIn("private key", suspicious_content(b"-----BEGIN " + b"OPENSSH PRIVATE KEY-----"))
        self.assertIn("private machine path", suspicious_content(b"/home/" + b"hermes/private-note"))
        for name in (".env.production", "state.db-wal", "state.db-shm", "cases.jsonl", "cookies.txt"):
            self.assertTrue(forbidden_filename(Path(name)))

    def test_no_obvious_secrets_or_runtime_state_in_commit_candidates(self):
        listing = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout
        paths = [Path(p.decode("utf-8")) for p in listing.split(b"\0") if p]
        self.assertTrue(paths, "empty repository")
        for relative in paths:
            with self.subTest(file=relative.as_posix()):
                self.assertFalse(forbidden_filename(relative), f"forbidden committed path: {relative}")
                source = ROOT / relative
                self.assertFalse(source.is_symlink(), f"symlink in portable source: {relative}")
                self.assertTrue(source.is_file(), f"missing committed file: {relative}")
                self.assertEqual(suspicious_content(source.read_bytes()), [], f"secret signature: {relative}")


    def test_inherited_git_history_has_no_obvious_secret_blobs(self):
        commits = subprocess.run(
            ["git", "rev-list", "--all"], cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout.splitlines()
        inspected = set()
        for commit in commits:
            entries = subprocess.run(
                ["git", "ls-tree", "-rz", commit], cwd=ROOT, check=True, capture_output=True,
            ).stdout.split(b"\0")
            for entry in entries:
                if not entry:
                    continue
                metadata, raw_path = entry.split(b"\t", 1)
                _, kind, oid = metadata.split(b" ", 2)
                if kind != b"blob":
                    continue
                relative = Path(raw_path.decode("utf-8"))
                self.assertFalse(forbidden_filename(relative), f"forbidden history path: {relative}")
                if oid in inspected:
                    continue
                inspected.add(oid)
                content = subprocess.run(
                    ["git", "cat-file", "blob", oid.decode("ascii")],
                    cwd=ROOT, check=True, capture_output=True,
                ).stdout
                self.assertEqual(suspicious_content(content), [], f"secret signature in history: {relative}")


if __name__ == "__main__":
    unittest.main()
