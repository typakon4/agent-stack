---
name: workflow-eval
description: Use before and after a model, setup, prompt, or skill change to compare a small fixed behavioral task set and record reliability, corrections, time, and available usage.
---

# Small workflow evaluation

Adapted from Affaan Mustafa's ECC eval-harness (MIT).

## Boundaries

- Preserve existing permissions and the repository's tests/handoff contract. This skill does not authorize a config/model/auth change, deployment, commit, upload, or memory replacement.
- Use local, disposable fixtures with no real user data. Do not collect raw prompts, transcripts, environment/auth files, private configs, or logs. Keep only reviewed task labels, pass/fail, aggregate metrics, and sanitized evidence references.
- No background collectors, new evaluation framework, mandatory coverage threshold, mandatory commits, or TDD override. Do not make extra API calls to fill a metrics table.

## Define once, compare fairly

1. **Freeze a tiny task set before the change.** Choose one to three representative tasks for the real workflow, with fixed inputs, the same allowed tools, a concrete behavioral pass/fail oracle, and an existing runnable command where possible. Record the runtime/version and the one variable being compared; do not change tasks or grading after seeing a failure.
2. **Run a baseline.** Execute each task once. Record first-attempt result before fixing anything; then record any corrective attempts separately. If the prior state is unavailable, say `baseline unmeasured` rather than reconstructing it.
3. **Apply only the authorized change.** Keep fixtures, grading, permissions, and other setup/model choices fixed. State unavoidable differences; do not attribute a gain to one variable if several changed.
4. **Run the same task set after the change.** Prefer behavioral assertions against actual outputs/state transitions and the real runtime surface.
5. **Compare and hand off.** Report regressions and strongest demonstrated result, including failures. Do not promote a change on aggregate scores that hide a failed safety boundary.

## Minimal result record

Use one row per task and phase:

`phase | task | first attempt PASS/FAIL | final PASS/FAIL | corrections | elapsed seconds | evidence`

A correction is an additional attempt after a failed result. Report first-attempt success as `first-attempt passes / tasks run` for that phase.

Add aggregate usage for the same run scope:

`input tokens | output tokens | cache read/write tokens | reasoning tokens | estimated USD`

Missing fields are `unmeasured`, never zero. Estimate USD only from observed usage and a known dated model tariff, explaining the formula; otherwise write `unmeasured`.
