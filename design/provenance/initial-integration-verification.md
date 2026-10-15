# Design integration verification — 2026-10-15

This report covers the integration of the supplied Hermes archive and the previously reviewed 29-skill Codex design bundle. The original author report is retained in `provenance/hermes-original-verification.md`; it is historical evidence, not a claim about this checkout.

## Integrated scope

- Shared `design-reference-loop`: original five files relocated to the existing shared-skill layout without byte changes; optional targets for Hermes, OMP and Codex.
- 29 static Codex skills: 85 byte-identical reviewed files, original licenses and explicit-only invocation metadata. Optional Codex targets only.
- 40 manifest components total; original nine entries and Jev pin preserved. Installer code and its source/target restrictions are unchanged.
- Design docs, templates, synthetic fixtures and the read-only offline checker; separate manual Codex routing fragment; design tests added to the existing Linux/Windows CI matrix.
- Exact upstream commits and file hashes in `source-lock.json`. Narrow `.gitattributes` rules preserve reviewed bytes across Git newline settings; whitespace checks for those immutable source files allow their existing upstream whitespace.

## Observed local checks

Windows, Python **3.12.10**, 2026-10-15:

| Check | Observed result |
| --- | --- |
| `python -B tests/validate_manifest.py` | OK, 40 components |
| `python -B -m unittest discover -s design/tests -v` | 19 tests passed: original 16 plus source hashes/static surface, optional/runtime boundaries, and full selected installs |
| `python -B -m unittest discover -s tests -v` | 10 tests passed, no skips, outside the desktop sandbox; includes PowerShell wrapper, Windows junction, 8.3 repository containment, current-candidate and Git-history obvious-secret checks |
| `python -B design/tools/review_candidates.py design/examples/candidates.json --decision design/examples/decision.fixture.json` | `proposal`, `selected_id: editorial`, `decision_provider: fixture`, user choice required, execution disabled, `cinematic` excluded |
| SkillSpector 2.12.0 static scans | Codex: maximum LOW 20/100, partial coverage. Original Hermes: MEDIUM 41/100, 17/17 components inspected. No HIGH/CRITICAL; all flagged locations manually reviewed. See `provenance/security-review.md`. |
| Native PowerShell selected preview | `installers/install.ps1 codex` with workflow, Taste, Emil and Impeccable selected: exit 0, four DRY-RUN entries, no apply |
| Git index and diff review | All 90 locked skill-file blobs match their SHA-256 before commit; `git diff --cached --check` passed; original nine manifest entries and Jev pin unchanged |

Design tests ran with TMP/TEMP redirected to a writable disposable test directory outside the repository. The initial default sandbox temp directory denied file access. With a writable temp root, the design suite passed; the baseline suite still exposed sandbox-only Python-launcher/8.3/junction limitations. The same unmodified baseline tests passed outside the sandbox. No implementation change was made to disguise those failures.

Selected-install tests proved dry-run leaves the disposable homes empty, Codex receives exactly 30 chosen skill directories with matching hashes, and Hermes/OMP receive only the chosen shared workflow. Baseline previews omit all optional design skills. Codex-only design components are refused for Hermes/OMP.

## Limits

No active runtime profile or global instructions were written. File installation into disposable homes does not prove runtime discovery, hot reload, tool availability or model adherence; all new `tested_on` lists remain empty. No live Jev adapter, paid LLM call, real design quality measurement, application UI test or claimed token saving is included. Linux and Python 3.14 execution depend on the configured CI; this report records only observed checks, not future CI success.
