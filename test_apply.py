"""One isolated check for dry-run, replacement backup, and blocked/secret skills."""

import subprocess
import sys
import tempfile
from pathlib import Path

from apply import source_files

REPO = Path(__file__).resolve().parent


def run(root, name, *flags):
    return subprocess.run(
        [sys.executable, str(REPO / "apply.py"), "--target", "PC_HERMES", "--skills-dir", str(root), "--skill", name, *flags],
        text=True, capture_output=True,
    )


def test():
    with tempfile.TemporaryDirectory(prefix="contour-check-", dir=Path.home()) as temporary:
        skills = Path(temporary) / "node" / "skills"
        name = "personal-operator-baseline"
        target = skills / name
        result = run(skills, name)
        assert result.returncode == 0 and "DRY-RUN" in result.stdout and not skills.exists(), result.stderr

        target.mkdir(parents=True)
        (target / "SKILL.md").write_text("old local skill\n")
        result = run(skills, name, "--apply")
        assert result.returncode == 0, result.stderr
        assert (target / "SKILL.md").read_bytes() == (REPO / "skills" / name / "SKILL.md").read_bytes()
        backups = list((skills.parent / "contour-skill-backups").glob("root--personal-operator-baseline--*"))
        assert len(backups) == 1 and (backups[0] / "SKILL.md").read_text() == "old local skill\n"

        blocked = run(skills, "multi-host-agent-operations", "--apply")
        assert blocked.returncode != 0 and not (skills / "devops" / "multi-host-agent-operations").exists()
        assert run(REPO / "skills", name, "--apply").returncode != 0

        sensitive = Path(temporary) / "sensitive"
        sensitive.mkdir()
        (sensitive / ".env.production").write_text("not-a-credential\n")
        try:
            source_files(sensitive)
        except ValueError:
            pass
        else:
            raise AssertionError("env file was accepted")


if __name__ == "__main__":
    test()
    print("isolated contour apply check: OK")
