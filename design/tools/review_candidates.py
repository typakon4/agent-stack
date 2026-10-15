"""Bounded, read-only design shortlisting; no network, model calls or execution."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import re
import sys

MAX_FILE_BYTES = 128_000
ID = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}\Z")


def text(value, limit=1200):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= limit


def identifier(value):
    return isinstance(value, str) and ID.fullmatch(value) is not None


def only_keys(value, allowed):
    return isinstance(value, dict) and set(value) <= set(allowed)


def validate(payload):
    if not only_keys(payload, ("schema_version", "request_id", "brief", "candidates")):
        raise ValueError("invalid packet fields")
    if type(payload.get("schema_version")) is not int or payload["schema_version"] != 1:
        raise ValueError("unsupported packet schema")
    if not identifier(payload.get("request_id")):
        raise ValueError("invalid request id")
    brief = payload.get("brief")
    if not only_keys(brief, ("goal", "surface", "required_checks")):
        raise ValueError("invalid brief")
    if not text(brief.get("goal")) or not text(brief.get("surface")):
        raise ValueError("brief requires a bounded goal and surface")
    checks = brief.get("required_checks")
    if (not isinstance(checks, list) or not 1 <= len(checks) <= 12
            or not all(identifier(check) for check in checks) or len(set(checks)) != len(checks)):
        raise ValueError("required checks must be unique identifiers")
    candidates = payload.get("candidates")
    if not isinstance(candidates, list) or not 2 <= len(candidates) <= 5:
        raise ValueError("provide two to five concepts")
    seen = set()
    for candidate in candidates:
        if not only_keys(candidate, ("id", "summary", "macrostructure", "vs_probability", "checks")):
            raise ValueError("invalid concept fields")
        cid = candidate.get("id")
        if not identifier(cid) or cid in seen:
            raise ValueError("concept ids must be unique")
        seen.add(cid)
        if not text(candidate.get("summary")) or not text(candidate.get("macrostructure"), 80):
            raise ValueError("concept requires a summary and macrostructure")
        probability = candidate.get("vs_probability")
        if probability is not None and (type(probability) not in (int, float)
                or not math.isfinite(probability) or not 0 <= probability <= 1):
            raise ValueError("invalid optional VS probability")
        values = candidate.get("checks")
        if not isinstance(values, dict) or not set(values) <= set(checks):
            raise ValueError("concept checks must match the brief")
        for check in values.values():
            if (not only_keys(check, ("status", "evidence"))
                    or check.get("status") not in ("pass", "fail", "unmeasured")
                    or not isinstance(check.get("evidence"), str)
                    or len(check["evidence"]) > 600):
                raise ValueError("invalid check result")
    return brief, candidates


def build_packet(payload):
    """Trust no quality probabilities; check supplied host attestations only.

    These assertions must be reviewed by the host/human. This utility does not
    independently verify them and is not an authorization or security boundary.
    """
    brief, candidates = validate(payload)
    eligible, excluded = [], []
    for candidate in candidates:
        values = candidate["checks"]
        passes = all(values.get(key, {}).get("status") == "pass"
                     and text(values.get(key, {}).get("evidence"), 600)
                     for key in brief["required_checks"])
        if passes:
            eligible.append({key: candidate[key] for key in ("id", "summary", "macrostructure")})
        else:
            excluded.append(candidate["id"])
    return {
        "schema_version": 1, "request_id": payload["request_id"],
        "status": "ready_for_review" if eligible else "no_eligible_candidates",
        "goal": brief["goal"], "surface": brief["surface"],
        "candidates": eligible, "excluded_ids": excluded,
        "execution": {"enabled": False},
    }


def review_decision(payload, decision):
    packet = build_packet(payload)
    result = {**packet, "status": "manual_review", "selected_id": None,
              "requires_user_choice": True, "decision_provider": None,
              "reason": "No usable decision; ask the user to review the eligible concepts."}
    if not only_keys(decision, ("schema_version", "request_id", "status", "candidate_id", "provider")):
        return result
    if (type(decision.get("schema_version")) is not int or decision["schema_version"] != 1
            or decision.get("request_id") != packet["request_id"]
            or decision.get("status") != "selected"
            or not text(decision.get("provider"), 80)):
        return result
    ids = {candidate["id"] for candidate in packet["candidates"]}
    selected = decision.get("candidate_id")
    if not identifier(selected) or selected not in ids:
        return result
    return {**result, "status": "proposal", "selected_id": selected,
            "decision_provider": decision["provider"],
            "reason": "Advisory shortlist only; user choice and implementation checks remain required."}


def load_json(path):
    with Path(path).open("rb") as stream:
        data = stream.read(MAX_FILE_BYTES + 1)
    if len(data) > MAX_FILE_BYTES:
        raise ValueError("input exceeds the file limit")
    return json.loads(data.decode("utf-8-sig"))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidates", help="Reviewed design packet JSON")
    parser.add_argument("--decision", help="Optional normalized advisory decision JSON (not raw jev_route output)")
    args = parser.parse_args(argv)
    try:
        payload = load_json(args.candidates)
        if args.decision:
            try:
                decision = load_json(args.decision)
            except (OSError, ValueError, UnicodeError):
                decision = None
            output = review_decision(payload, decision)
        else:
            output = build_packet(payload)
    except (OSError, ValueError, UnicodeError):
        print("Invalid or unreadable design packet; no input content was printed.", file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
