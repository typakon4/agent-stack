"""Portability and package integrity, not model-behavior or UI evaluation."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent


class PackIntegrity(unittest.TestCase):
    def test_skill_frontmatter_and_referenced_files(self):
        skill = REPO / "shared" / "skills" / "design-reference-loop" / "SKILL.md"
        body = skill.read_text(encoding="utf-8")
        self.assertTrue(body.startswith("---\nname: design-reference-loop\n"))
        for reference in re.findall(r"`(references/[^` ]+\.md)`", body):
            self.assertTrue((skill.parent / reference).is_file(), reference)
        self.assertEqual(len(re.findall(r"`(references/[^` ]+\.md)`", body)), 4)

    def test_markdown_local_links_resolve_inside_repository(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (path.parent / target.split("#")[0]).resolve()
                with self.subTest(file=path.relative_to(ROOT), link=target):
                    self.assertTrue(resolved.is_relative_to(REPO.resolve()))
                    self.assertTrue(resolved.exists())

    def test_user_extension_point_and_templates_exist(self):
        expected = ["user-library/README.md", "templates/brief.md", "templates/direction.md",
                    "templates/feedback.md", "templates/handoff.md", "README.md"]
        for item in expected:
            with self.subTest(file=item):
                self.assertGreater(len((ROOT / item).read_text(encoding="utf-8").strip()), 50)


if __name__ == "__main__":
    unittest.main()
