# Design import security review — 2026-10-15

## Candidate and authority

- Hermes: user-supplied `agent-stack-design-pack-local-v1.zip`, SHA-256 `a134ea9b91247e6193883586b4ea03213ad250ebe9f6740825e5e01beebaedf1`; 17 entries, archive CRC check passed. Paths were checked for traversal, absolute paths, duplicate names and symlinks before staging.
- Codex: the previously reviewed local static bundle, 29 skills / 85 files. All file hashes matched both its original bundle manifest and the installed local copies before import. Source commits and notices are preserved in `../source-lock.json`; no upstream update was performed.
- The user requested integration and push. Prior approval explicitly selected static Impeccable rules without its engine/hooks; that boundary is preserved. Source documents are review data, not permission to execute their examples.

## Runtime surface and manual review

- Codex payload: Markdown, license text and three YAML metadata files containing only `policy.allow_implicit_invocation: false`. No executable, hook, launcher, server, MCP registration or setup dependency is shipped. Each skill retains its local policy override; Impeccable retains its static adaptation notice and Apache-2.0 license.
- Hermes workflow and references are static. The repository-only `review_candidates.py` uses stdlib argument parsing, bounded JSON reads and stdout; no network, model invocation, subprocess, file writes or dynamic execution. IDs are validated and returned only as advisory data. Supplied attestations are not independently verified.
- Hermes tests import that checker and invoke it using explicit `subprocess.run` argument lists with the current Python interpreter; `shell=False` is the default. Their only writes are disposable fixtures. The new integration tests exercise the existing reviewed installer in disposable runtime homes.
- The original installer and its path/secret protections are unchanged. Manifest entries are optional; the routing fragment is manual. No active profile is written during integration.

## SkillSpector

Installed pinned SkillSpector **2.12.0**, static `scan --no-llm`; no provider credentials or semantic LLM analysis. Reports were written outside the repository. The initial nested staging-root scan did not discover sub-skills and was stopped; the two completed scans targeted the actual Codex skill collection and Hermes package separately.

| Completed scan | Observed result | Coverage limits |
| --- | --- | --- |
| Codex collection, `--recursive` | 29 scanned, 0 omitted; maximum 20/100 LOW; no HIGH/CRITICAL; CAUTION recommendation | Partial analysis: 11 skills complete, 18 partial; reported completeness 37.93%. Generated example references and parser limits remain unresolved. |
| Original Hermes package | 41/100 MEDIUM; 6 MEDIUM occurrences; no HIGH/CRITICAL; CAUTION recommendation | Static analysis reported 17/17 components complete; semantics and model behavior were not evaluated. |

Every LOW/MEDIUM location in the final reports was inspected before accepting this import. Repeated occurrences may share a finding ID; a grouped finding count is not the number of source locations.

### Hermes dispositions (paths before relocation)

| Finding / location | Inspected content and disposition |
| --- | --- |
| AE4, `README.md:1` | Mixed Russian/English documentation; no hidden execution or authority change identified. |
| AS3, `README.md:7` and `:17` | Explicit references to this package's own workflow, not enumeration of a host's installed private skills. |
| EA2, `skills/design-reference-loop/references/ui-proof.md:3` | The matched phrase is a prohibition on adding frameworks/starting services before checking scope. |
| AST4, `tests/test_review_candidates.py:104` and `:116` | Fixed Python/checker/fixture argument lists with no shell interpolation. Malformed input is tested without echoing its contents. |

### Codex dispositions (paths relative to each skill)

| Finding / location | Inspected content and disposition |
| --- | --- |
| RP1, `animate-expo/RECIPES.md:10,258`; `animate-expo/SKILL.md:89,215` | Expo package-installation examples. No installation was executed; local skill policy requires scope, compatible versions and user authorization. |
| RA2, `animate-expo/SKILL.md:225` | iOS frame-rate `infoPlist` example, not host persistence. It remains optional project code subject to authorization. |
| EA2, `design-taste-frontend/SKILL.md:56`; `design-taste-frontend-v1/SKILL.md:18`; `imagegen-frontend-web/SKILL.md:104` | Conversational override of style dials rather than asking the user to edit skill files. Does not override approval policy. |
| RP1, `design-taste-frontend/SKILL.md:104,1033,1034` | shadcn dependency examples, including `@latest`. Retained source text is not an approved version choice or permission to install. |
| RA2, `imagegen-frontend-mobile/SKILL.md:75` | Substring match inside “simplistic”; no plist file or persistence action. |
| EA2, `impeccable-design/references/audit.md:138` | “Report false positives without verification” occurs in a NEVER list. |
| EA3 LOW, `impeccable-design/LICENSE:56` | Apache license wording “not limited to”; the legal text is preserved. |

## Decision and residual risk

**Safe to consider within the authorized static scope.** Import only the reviewed bytes and the documented workflow; keep all design skills optional and Codex adaptations scoped to Codex. No extra install/enable approval is needed for the requested repository import/publication; activation in another runtime/profile is outside this change.

The scan is a gate, not proof of safety. Partial static coverage, instructions that can conflict with project needs, dependency examples, aesthetic quality and model adherence remain limitations. No paid model call, real Jev choice, application UI test, independent behavioral audit or token-savings measurement was performed. Future source updates or executable integration require a new review.
