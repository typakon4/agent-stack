# Local verification and handoff

## Scope

Local-only draft in branch `design/local-pack`, based on agent-stack commit `4295a2f2bcde5394cc840d4ee9abe92ef1e44e5f`. All new source is inside `design/`. No tracked upstream files, root manifest, Jev pin, installed skills, credentials or runtime configuration changed. No commit, push, release or deployment was performed.

## Executed checks

Linux, Python 3.14.7:

- `python -m unittest discover -s design/tests -v`: **16 tests passed**. Covers required constraints, unknown/excluded/stale choices, missing advice, unmeasured checks, duplicate ids, invalid probabilities, synthetic CLI execution, local links and extension templates.
- `python tests/validate_manifest.py`: **OK, 9 existing components**. The design draft is intentionally not registered with the installer.
- `python -m unittest discover -s tests -v`: **OK, 10 tests run, 2 skipped**. PowerShell unavailable and Windows 8.3-path test not applicable on Linux. Includes the repository's obvious-secret/current-candidate/history checks; these do not prove absence of every possible secret.
- `python design/tools/review_candidates.py design/examples/candidates.json --decision design/examples/decision.fixture.json`: actual stdout reported `status: proposal`, `selected_id: editorial`, `decision_provider: fixture`, `requires_user_choice: true`, `execution.enabled: false`; `cinematic` was excluded.
- Git status showed only the new `design/` files; tracked diff was empty. No unrelated project/profile edits were made.

The new behavioral tests were first run without the implementation and failed because the checker module did not exist; they passed after the implementation was added.

## What this evidence does not prove

- No real Jev/TypeSafe/OpenRouter or VS model call was made.
- No real design candidate quality or model adherence was measured.
- No application UI was built, visually approved or exercised by this pack's synthetic example.
- No Windows runtime test was performed.
- The helper checks supplied host-reviewed attestations; it does not independently establish them or act as a security boundary.

## Next owner decisions

Add your reviewed design materials under `user-library/` and refer to them explicitly in a project brief. A future runtime installation, manifest integration, live Jev adapter or GitHub publication requires its own approval and verification. The unavailable pinned Jev revision was not replaced. Keep this folder out of active profiles until its intended host/runtime and content are reviewed.
