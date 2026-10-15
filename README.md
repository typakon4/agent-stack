![agent-stack — 3 agents. one ruleset.](assets/agent-stack-cover.jpg)

# agent-stack

**Keep your working rules when you change agents.**

Portable, reviewed instructions, skills and templates for **Hermes, OMP and Codex**. Share a selected behavior baseline; keep credentials, runtime settings and live sessions local.

[Quick start](#preview-first) · [Components](#pick-one-component) · [Compatibility](docs/compatibility.md) · [Security](docs/security.md)

> **“One ruleset” means a shared baseline, not universal compatibility.** Each component has explicit runtime targets and limits in [`manifest.yaml`](manifest.yaml). Reviewed content is not proof of identical model behavior.

## What travels / what stays local

| Share after review | Keep with the runtime / host |
| --- | --- |
| Verification instructions | Credentials, OAuth stores and provider keys |
| Selected skills with explicit targets | Model/provider settings and MCP registration |
| Blank handoff templates | Live sessions, logs, schedules and databases |
| Sanitized operating rules | Profile identity, machine config and private knowledge |

This is **not** a runtime installer, configuration backup or session-sync service. It does not upgrade Hermes, OMP, Codex or Jev, replace native configuration, or automatically pull, push or deploy.

## Preview first

Python **3.12+** is the supported validation baseline. From the repository root, list reviewed components without writing:

```sh
./installers/install.sh hermes
# or: omp / codex
```

On Windows:

```powershell
./installers/install.ps1 codex
```

To inspect one skill against the selected Hermes profile, first set `HERMES_HOME` to its **existing absolute runtime root**, then preview:

```sh
./installers/install.sh hermes \
  --component proof-gated-coding-delivery \
  --destination "$HERMES_HOME" \
  --no-clobber \
  --dry-run
```

Read the plan before changing anything. Only after approving the exact component and destination, replace `--dry-run` with `--apply`.

- `--apply` requires both a named component and an explicit destination.
- The destination is a runtime home, never this repo or the runtime's source checkout.
- `--no-clobber` refuses existing selected targets. Without a destination, the preview cannot check local collisions.
- Intentional replacement without `--no-clobber` preserves the old target in a backup; review and restore it manually when needed.
- Optional components require explicit selection. Manual fragments are for human merge and cannot be installed by the helper.

More examples and rollback details: [portability](docs/portability.md).

## Pick one component

| Component | Targets | Adoption |
| --- | --- | --- |
| `verification` | Hermes / OMP / Codex | Reviewed instruction text; installation does not auto-load it |
| `proof-gated-coding-delivery` | Hermes / OMP / Codex | Reviewed skill: distinguish implementation, local runtime proof and release readiness |
| `knowledge-combine` | Hermes / OMP / Codex | Optional knowledge curation; requires a user-selected location |
| `handoff-template` | Hermes / OMP / Codex | Optional blank template, not session synchronization |
| `ecc-context-budget` / `ecc-workflow-eval` | Hermes / OMP | Optional selective ECC adaptations with documented offline checks |
| `personal-operator-baseline` | Hermes only | Reviewed Hermes-specific behavior |
| `hermes-soul-fragment` / `codex-agents-fragment` | Their respective runtime | Manual merge; preserve existing local policy |

The [manifest](manifest.yaml) is authoritative for status, destinations, dependencies and `tested_on`. `reviewed` does not mean every version, host, profile or UI was exercised. Do not infer support from a matching skill name. See [compatibility](docs/compatibility.md).

## How the pack fits

```text
shared content + explicit manifest targets
                    |
              preview one component
                    |
          approve the exact destination
                    |
        apply, then verify in that runtime
```

Each runtime retains its own executables, configuration, identity, permissions and state. A shared skill can describe a process; it cannot authorize external actions. See [architecture](docs/architecture.md).

## Installed is not loaded

The selective ECC trial documents actual offline discovery/read and fixed loader/dry-run checks for OMP and Windows Hermes. A fresh OMP CLI saw the new resources while an already-running conversation did not adopt them. File installation is not proof of hot reload, model adherence, quality improvement or token savings.

Read the [recorded trial and limitations](docs/portability.md#selective-ecc-adaptations) before making a support or performance claim. The adaptations retain pinned upstream credit and MIT notices.

The separate optional [native ECC trial](runtimes/omp/README.md#native-ecc-trial-ecc-safe) uses a pinned Pi adapter in an isolated OMP profile. Its PowerShell 7 launcher keeps additional ECC rules and lifecycle scripts disabled. It does not replace default OMP policy or the two curated skills.

## Security and ownership

Both previews and installs check selected sources for obvious secret/state filenames and credential signatures without printing matched values. This is a guard, **not a complete secret detector**. Human source and staged-diff review is still required.

Never export credentials, browser profiles, private vaults, raw conversations or runtime state through this pack. A tool being authenticated is not permission to publish, push, buy, send, delete or deploy. See the [security boundaries](docs/security.md).

Jev remains an **external dependency**, pinned to `08473a5496864e8c97ee6f8f58980131ae16aed2`. This repository contains no Jev source, MCP config, credentials or replay. See [Jev integration](integrations/jev/README.md).

## Validate

```sh
python tests/validate_manifest.py
python -m unittest discover -s tests -v
```

GitHub Actions runs the same checks on Linux and Windows with Python 3.12 and 3.14, plus native installer previews. The obvious-secret scan includes full Git history. Local installer regression tests use disposable runtime homes, not real profiles. Runtime/model adherence and the optional native ECC trial are separate from repository CI.

## Add a skill or runtime

Review tool assumptions, privacy, provenance and publication boundaries. Add explicit targets/status to the manifest, then dry-run against the actual approved destination. Preserve native policy rather than replacing whole configurations.

The five baseline commits remain in history for provenance; obsolete Hermes-only files are absent from the current tree.

<sub>Cover: user-generated illustration featuring Rei Ayanami, a third-party fictional character. Unofficial; no affiliation with Evangelion or the named runtime projects. The illustration is not runtime evidence.</sub>
