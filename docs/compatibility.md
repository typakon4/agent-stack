# Compatibility and ownership

| Runtime | Portable components | Local integration and boundaries |
| --- | --- | --- |
| Hermes | Shared verification and proof-gated skill; optional knowledge-combine and handoff; Hermes-only operator skill; manual SOUL fragment | Existing selected profile owns its SOUL, gateway, credentials, and local state. Jev uses a thin manually configured plugin plus MCP where supported. No PC Hermes install or VPS service change here. |
| OMP | Shared verification and proof-gated skill; optional knowledge-combine and handoff | Preserve current Graphify/CodeGraph/ripgrep, Ponytail, i-have-adhd, diff-shrink, LSP, subagents, RTK, and existing Jev stdio MCP. No replacement policy, Jev config, or duplicate endpoint. |
| Codex | Shared verification and proof-gated skill; optional knowledge-combine and handoff; manual AGENTS fragment | Jev integration is MCP configured in Codex's own runtime, not by this repository. Merge only the ten portable AGENTS rules in the appropriate local scope; leave project rules and absolute imports local. |

`reviewed` means selected portable content has been reviewed for that target, **not** that every profile, version, host, or UI has been exercised. `optional` requires an explicit named use case; `manual` is for a human merge, never an installer overwrite. Check `manifest.yaml` for authoritative component status, dependencies, and `tested_on`; do not turn an empty or limited test record into a support claim. Verify the actual local installation/behavior after an authorized apply.

The [design stack](../design/README.md) adds optional runtime-neutral `design-reference-loop` text for Hermes/OMP/Codex and 29 optional **Codex-only** static adaptations. Their selected installation is exercised in disposable homes; actual runtime discovery and model behavior after adoption remain untested (`tested_on: []`). Image generation, browser interaction, document rendering and other specialized tools must be supplied by the selected runtime. This pack does not grant or install them, and the Jev concept-selection contract remains offline.
