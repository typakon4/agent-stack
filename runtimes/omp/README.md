# OMP mapping

OMP keeps its current coding policies and optimized toolchain: Graphify/CodeGraph/ripgrep, Ponytail full, i-have-adhd, diff-shrink, LSP, specialized subagents, and RTK Pi-compatible tooling. Portable skills and verification instructions **add to** those rules; a copied instruction never supersedes local policy or a project's instructions.

Keep OMP's existing Jev **stdio MCP** integration. Do not copy/overwrite its MCP config, extensions, model roles, local subagents, LSP paths, credentials, or replay. Jev's MCP decisions are advisory: no automatic provider/model/thinking changes or context deletion. Avoid a duplicate Jev extension or second server instance. Select the existing OMP runtime root explicitly and preview before installation; do not install a Hermes SOUL or operator skill here.

## Native ECC trial: `ecc-safe`

The ready upstream Pi adapter is exercised in a separate local OMP profile, not installed into the default profile. Source: `~/Documents/ECC-ef648e01899b`, detached at ECC commit `ef648e01899ba3e8dc6371642deaaf64b4477775` (2.2.3). Keep this trusted checkout unchanged; the launcher checks HEAD, not every working-tree file. The extension remains unsandboxed code.

### Start

PowerShell 7, existing Node and Git are required:

```powershell
pwsh -NoProfile -File "$HOME\Documents\agent-stack\runtimes\omp\ecc-safe.ps1"
```

`-Workspace <existing-directory>` selects a project. `-Model <native-selector>` selects a model for that session only, including native `:thinkingLevel`/`@upstream` syntax. The default `openai/gpt-5.2` is a catalog choice used for credential-free loader smoke, not a model recommendation or a copied model role. `-Check` previews validated paths/pin/arguments without starting OMP; `-Rpc -NoSession` exposes the actual JSONL runtime for no-model diagnostics.

The isolated profile has no copied credentials. Authenticate through OMP's own provider flow in that profile before real model work; never paste credentials into a handoff or copy the default profile's auth file. First-run setup can be canceled with its documented Ctrl+C action. Our TUI smoke canceled it without entering credentials; OMP recorded `setupVersion: 2` only in the trial profile.

### Selected capabilities

| Resource | Added behavior |
|---|---|
| `search-first` | Compare existing tools/libraries before deciding to adopt, extend or build. |
| `security-review` | Focused auth, input validation, secrets and data-exposure checklist. |
| `/ecc-code-review` | Explicit local code-review prompt with severity, locations and proposed fixes. |
| `/ecc-doctor` | Actual upstream adapter diagnostic: source root/version, rules and hook status. |

Ponytail, proof-gated delivery, `ecc-context-budget` and `ecc-workflow-eval` remain available on demand: six skill commands total. Only the two selected upstream skill bodies are eligible from the ECC catalog. The review template is local-only: do not supply a PR number/URL or publish a review implicitly. Upstream install/audit-fix/pseudo-agent examples do not override host/project policy or authorize dependency/config changes.

### Isolation

`ecc-safe.ps1` starts the fixed named profile/config and exact `.pi/extensions/index.ts` with `--trusted-extension`; package-directory sibling MCP/hooks/rules/agents are not authorized. It disables ambient extension/rule loading, keeps foreign discovery and MCP JSON discovery disabled in this profile, and supplies existing verification instructions. This is not a whole-process sandbox; selected project instructions and native tools retain their authority.

ECC rules and lifecycle scripts are disabled through child-only environment variables. ECC data-home/homunculus overrides point inside the trial profile as an additional boundary. Two lightweight Node runner processes still occur at startup/shutdown; their gate skips the lifecycle scripts. No global environment/settings were changed. Direct `omp --profile ecc-safe` loads resources only: the adapter is deliberately absent from profile extension configuration, so use the launcher for adapter diagnostics.

Doctor's 293 skills/94 commands are raw canonical source counts, not enabled-resource counts. Its optional Pi-companion suggestions do not detect OMP's native todos/subagents/MCP; do not install those companions on that basis.

### Exercised proof — 2026-10-06

Actual OMP 18.6.0/PowerShell 7 RPC startup discovered the adapter command, local review template and exactly six skills. `/ecc-doctor` completed locally; the actual `prompt_result` reported `agentInvoked: false`. Diagnostic history, Unicode/space-containing workspace and native `:high` selector were verified. Real Node lifecycle receipts showed both runners exiting 0 with scripts disabled; no ECC memory directories were created. Default config/auth file metadata was unchanged during the final smoke.

The actual TUI also rendered `/ecc-doctor`; both RPC EOF and TUI double-Ctrl+C shutdown exited 0. Temporary tracing was removed. No model inference task, semantic skill/template adherence, review publication, token savings or quality gain was tested. Hermes/VPS/default OMP/Jev/Mnemopi were not migrated or configured by this trial.

