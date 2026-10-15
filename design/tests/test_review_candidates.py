"""Offline contract checks. Fixtures are synthetic, not model/browser evidence."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("review_candidates", ROOT / "tools" / "review_candidates.py")
assert spec is not None and spec.loader is not None
review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(review)


class CandidateContract(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads((ROOT / "examples" / "candidates.json").read_text(encoding="utf-8"))
        self.decision = json.loads((ROOT / "examples" / "decision.fixture.json").read_text(encoding="utf-8"))

    def test_packet_excludes_failed_constraints_without_selecting(self):
        result = review.build_packet(self.payload)
        self.assertEqual([c["id"] for c in result["candidates"]], ["editorial", "release-console"])
        self.assertEqual(result["excluded_ids"], ["cinematic"])
        self.assertFalse(result["execution"]["enabled"])
        self.assertNotIn("selected_id", result)

    def test_valid_decision_is_only_a_proposal(self):
        result = review.review_decision(self.payload, self.decision)
        self.assertEqual(result["status"], "proposal")
        self.assertEqual(result["selected_id"], "editorial")
        self.assertTrue(result["requires_user_choice"])
        self.assertFalse(result["execution"]["enabled"])

    def test_absent_decision_preserves_manual_choice(self):
        result = review.review_decision(self.payload, None)
        self.assertEqual(result["status"], "manual_review")
        self.assertIsNone(result["selected_id"])
        self.assertEqual(len(result["candidates"]), 2)

    def test_unknown_failed_and_wrong_request_are_not_selected(self):
        changes = ({"candidate_id": "unknown"}, {"candidate_id": "cinematic"},
                   {"request_id": "another-request"}, {"status": "fallback"},
                   {"status": "no_decision"}, {"schema_version": 2},
                   {"provider": ""}, {"unexpected_command": "not-an-operation"})
        for change in changes:
            with self.subTest(change=change):
                result = review.review_decision(self.payload, {**self.decision, **change})
                self.assertEqual(result["status"], "manual_review")
                self.assertIsNone(result["selected_id"])
                self.assertFalse(result["execution"]["enabled"])

    def test_unmeasured_check_is_not_eligible(self):
        self.payload["candidates"][0]["checks"]["within_scope"]["status"] = "unmeasured"
        self.assertEqual([c["id"] for c in review.build_packet(self.payload)["candidates"]], ["release-console"])

    def test_missing_check_or_evidence_is_not_eligible(self):
        del self.payload["candidates"][0]["checks"]["within_scope"]
        self.payload["candidates"][1]["checks"]["within_scope"]["evidence"] = ""
        self.assertEqual(review.build_packet(self.payload)["status"], "no_eligible_candidates")

    def test_vs_probability_does_not_select_or_rank(self):
        before = review.build_packet(self.payload)
        self.payload["candidates"][0]["vs_probability"] = 0.99
        self.payload["candidates"][1]["vs_probability"] = 0.001
        self.assertEqual(review.build_packet(self.payload), before)
        self.assertEqual(review.review_decision(self.payload, self.decision)["selected_id"], "editorial")

    def test_duplicate_candidate_ids_are_invalid(self):
        self.payload["candidates"][1]["id"] = "editorial"
        with self.assertRaises(ValueError):
            review.build_packet(self.payload)

    def test_empty_checks_and_duplicate_checks_are_invalid(self):
        for checks in ([], ["within_scope", "within_scope"]):
            with self.subTest(checks=checks), self.assertRaises(ValueError):
                payload = copy.deepcopy(self.payload)
                payload["brief"]["required_checks"] = checks
                review.build_packet(payload)

    def test_invalid_schema_and_probability_are_invalid(self):
        for value in (True, -0.1, 1.1, float("nan")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                payload = copy.deepcopy(self.payload)
                payload["candidates"][0]["vs_probability"] = value
                review.build_packet(payload)
        self.payload["schema_version"] = True
        with self.assertRaises(ValueError):
            review.build_packet(self.payload)

    def test_no_eligible_candidates_never_get_a_selection(self):
        for candidate in self.payload["candidates"]:
            candidate["checks"]["within_scope"]["status"] = "fail"
        result = review.review_decision(self.payload, self.decision)
        self.assertEqual(result["status"], "manual_review")
        self.assertEqual(result["candidates"], [])
        self.assertIsNone(result["selected_id"])

    def test_cli_returns_structured_fixture_proposal(self):
        command = [sys.executable, str(ROOT / "tools" / "review_candidates.py"),
                   str(ROOT / "examples" / "candidates.json"), "--decision",
                   str(ROOT / "examples" / "decision.fixture.json")]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        parsed = json.loads(result.stdout)
        self.assertEqual(parsed["status"], "proposal")
        self.assertEqual(parsed["decision_provider"], "fixture")
        self.assertFalse(parsed["execution"]["enabled"])
        self.assertEqual(result.stderr, "")

    def test_invalid_input_cli_does_not_print_input(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text("not JSON: PRIVATE_FIXTURE_MARKER", encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT / "tools" / "review_candidates.py"), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("PRIVATE_FIXTURE_MARKER", result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
