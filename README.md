# agent-stack

Portable, reviewed agent behavior for **Hermes, OMP, and Codex**. This repository is not a runtime installation, configuration backup, or state synchronization service. The five baseline commits are retained for provenance; obsolete Hermes-only files are absent from the current tree.

## Use

Run `./installers/install.sh omp` (or `hermes` / `codex`) to preview reviewed components; on Windows use `./installers/install.ps1 codex` in PowerShell. An optional component needs an explicit `--component knowledge-combine`. To apply one component, pass its name, an **existing absolute runtime root** via `--destination`, and `--apply`; omit `--apply` for a read-only dry-run. Manual fragments are read and merged by a human, not applied by the installer. See [portability](docs/portability.md) for examples and [compatibility](docs/compatibility.md) for target restrictions.

Python 3.12+ is the supported validation baseline. Use `--no-clobber` with a destination to refuse existing targets before any installation; omit it only for an intentional replacement with backup. Both previews and installs reject obvious secret/state filenames and credential signatures without printing credential values. This is a guard, not a complete secret detector.

`shared/skills/` contains reviewed portable coding behavior, optional knowledge curation, and the selectively adapted `ecc-context-budget` / `ecc-workflow-eval` skills (OMP/Hermes only); `shared/instructions/verification.md` and `shared/templates/handoff.md` are reusable text. The ECC skills require explicit component selection and load on demand; [portability](docs/portability.md#selective-ecc-adaptations) records pinned credit, invocation, offline proof, and the current-session registry limitation. `runtimes/` documents local mapping; the Hermes operator skill is Hermes-only. To add a skill or runtime, review its tools, privacy and publication boundaries, add its explicit targets/status to `manifest.yaml`, then dry-run against the actual destination. Do not infer compatibility from a matching skill name.

The optional [native ECC trial](runtimes/omp/README.md#native-ecc-trial-ecc-safe) uses a pinned upstream Pi adapter in an isolated local OMP profile. Its PowerShell 7 launcher keeps extra ECC rules/lifecycle scripts disabled; actual RPC/TUI diagnostics and selected-resource discovery are verified. It does not replace the default OMP setup or the two curated skills.

Jev is an **external dependency**, pinned here to commit `08473a5496864e8c97ee6f8f58980131ae16aed2`. See [Jev integration](integrations/jev/README.md); this repository contains no Jev source, MCP config, credentials, or replay.

Review the [architecture](docs/architecture.md) and [security boundaries](docs/security.md). No automatic pull, push, or deployment occurs. The official Hermes updater owns Hermes itself; OMP and Codex retain their existing native configuration.

## Validate

```sh
python tests/validate_manifest.py
python -m unittest discover -s tests -v
```

GitHub Actions runs the same checks on Linux and Windows with Python 3.12 and 3.14, plus the native installer previews. Full Git history is included in the obvious-secret scan. Local installer regression tests use disposable runtime homes, never real profiles. Runtime/model adherence and the optional native ECC trial are separate from repository CI.
