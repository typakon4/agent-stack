---
name: ecc-workflow-eval
description: Use before and after a model, setup, prompt, or skill change to compare a small fixed behavioral task set and record reliability, corrections, time, and available usage.
license: MIT
---

# Small workflow evaluation

Adapted from Affaan Mustafa's [ECC eval-harness](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/eval-harness/SKILL.md), commit `ef648e01899ba3e8dc6371642deaaf64b4477775` (MIT; notice in `LICENSE`). Use the smallest runnable check, not ECC's framework or utilities.

## Boundaries

- Preserve Ponytail, proof-gated delivery, Jev routing, Mnemopi, existing task permissions, and the repository's tests/handoff contract. This skill does not authorize a config/model/auth change, deployment, commit, upload, or memory replacement.
- Use local, disposable fixtures with no real user data. Do not collect raw prompts, transcripts, environment/auth files, private configs, or logs. Keep only reviewed task labels, pass/fail, aggregate metrics, and sanitized evidence references.
- No background collectors, new evaluation framework, mandatory coverage threshold, mandatory commits, or TDD override. Do not make extra API calls to fill a metrics table. Paid model trials require the host's existing authorization; a local loader check needs none.

## Define once, compare fairly

1. **Freeze a tiny task set before the change.** Choose one to three representative tasks for the real workflow, with fixed inputs, the same allowed tools, a concrete behavioral pass/fail oracle, and an existing runnable command where possible. Include a real boundary case only when relevant. Record the runtime/version and the one variable being compared; do not change tasks or grading after seeing a failure.
2. **Run a baseline.** Execute each task once. Record first-attempt result before fixing anything; then record any corrective attempts separately. If the prior state is unavailable, say `baseline unmeasured` rather than reconstructing it. A new capability can intentionally fail before the change; distinguish that from a regression.
3. **Apply only the authorized change.** Keep fixtures, grading, permissions, and other setup/model choices fixed. State unavoidable differences; do not attribute a gain to one variable if several changed.
4. **Run the same task set after the change.** Prefer behavioral assertions against actual outputs/state transitions and the real runtime surface. Checking that a source file contains a function name, keyword, or desired skill prose is not a behavioral grader. Loader discovery/read proves availability, not semantic model compliance. Use human review for open-ended quality or security conclusions that the deterministic check cannot establish.
5. **Compare and hand off.** Report regressions and strongest demonstrated result, including failures. Do not promote a change on aggregate scores that hide a failed safety boundary. Use the existing `shared/templates/handoff.md` sections if a handoff is needed; do not create another live-state format.

## Minimal result record

Use one row per task and phase:

`phase | task | first attempt PASS/FAIL | final PASS/FAIL | corrections | elapsed seconds | evidence`

A correction is an additional attempt after a failed result, not a hidden replacement of the first result. Report first-attempt success as `first-attempt passes / tasks run` for that phase. This is a small-sample observation, not a statistically established reliability claim. Do not claim pass@k or repeated-run stability unless those controlled trials actually ran; extra repetitions are not required.

Add aggregate usage for the same run scope when the harness exposes it:

`input tokens | output tokens | cache read/write tokens | reasoning tokens | estimated USD`

Missing fields are `unmeasured`, never zero. Reasoning tokens may be included in output; cache tokens may be subsets of input. Preserve the provider's accounting rather than adding overlapping counters. Estimate USD only from observed usage and a known dated model tariff, explaining the formula and cache treatment; otherwise write `unmeasured`. Do not equate a subscription, elapsed time, or offline check with a token-based bill. Record whether timing includes startup/tool work, and whether cache state is controlled or unknown.

## Safe installation example

For a selective skill transfer, freeze these tasks before applying:

- **Regression:** an existing skill still loads through the host's actual catalog/read surface.
- **Capability:** the selected new skills are discoverable and their bodies load through that same surface. Before installation, expected absence is a capability baseline failure, not a broken regression. After installation, assert loader success and correct resolved artifact; source-text grep is not proof.
- **Safety:** the existing installer's dry-run produces a plan while the selected destination remains unchanged. Compare destination state, not an `APPLY` keyword in output.

Run the same checks after installation, once each. Record pass/fail, corrections, and wall time; usage/cost/context metrics remain `unmeasured` unless the actual harness reports them. Do not call a model just to populate those fields. This is a deterministic loader/safety smoke, not a benchmark of the model's understanding. A semantic comparison needs representative authorized model tasks and separate evidence.
