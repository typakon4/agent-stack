# agent-stack

Portable, reviewed agent behavior for **Hermes, OMP, and Codex**. This repository is not a runtime installation, configuration backup, or state synchronization service. The five baseline commits are retained for provenance; obsolete Hermes-only files are absent from the current tree.

## Use

Run `./installers/install.sh omp` (or `hermes` / `codex`) to preview reviewed components; on Windows use `./installers/install.ps1 codex` in PowerShell. An optional component needs an explicit `--component knowledge-combine`. To apply one component, pass its name, an **existing absolute runtime root** via `--destination`, and `--apply`; omit `--apply` for a read-only dry-run. Manual fragments are read and merged by a human, not applied by the installer. See [portability](docs/portability.md) for examples and [compatibility](docs/compatibility.md) for target restrictions.

`shared/skills/` contains reviewed portable coding behavior and optional knowledge curation; `shared/instructions/verification.md` and `shared/templates/handoff.md` are reusable text. `runtimes/` documents local mapping; the Hermes operator skill is Hermes-only. To add a skill or runtime, review its tools, privacy and publication boundaries, add its explicit targets/status to `manifest.yaml`, then dry-run against the actual destination. Do not infer compatibility from a matching skill name.

Jev is an **external dependency**, pinned here to commit `08473a5496864e8c97ee6f8f58980131ae16aed2`. See [Jev integration](integrations/jev/README.md); this repository contains no Jev source, MCP config, credentials, or replay.

Review the [architecture](docs/architecture.md) and [security boundaries](docs/security.md). No automatic pull, push, or deployment occurs. The official Hermes updater owns Hermes itself; OMP and Codex retain their existing native configuration.
