![agent-stack — 3 agents, one shared ruleset](assets/agent-stack-cover.jpg)

# agent-stack

**Keep your working rules when you change agents.**

Reviewed instructions, skills and templates for **Hermes, OMP and Codex**. Share a selected behavior baseline; keep credentials, runtime settings and live sessions with their owner.

[English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md)

[Quick start](#preview-first) · [Components](#pick-your-components) · [Design](design/README.md) · [Codex Cloud (RU)](docs/codex-cloud.md) · [Compatibility](docs/compatibility.md) · [Security](docs/security.md)

Each component has explicit targets and limits in [manifest.yaml](manifest.yaml). Shared targets let you install the same skill text into different runtimes. Identical model behavior and tool availability require separate verification.

## What travels

| Shared material | Stays with the runtime and host |
| --- | --- |
| Verification instructions | Credentials, OAuth stores and provider keys |
| Selected skills with explicit targets | Model/provider settings and MCP registration |
| Blank handoff templates | Live sessions, logs, schedules and databases |
| Reviewed working rules | Profile identity, machine settings and private knowledge |

This repository distributes behavior material. It does not upgrade Hermes, OMP, Codex or Jev, replace their configuration, or synchronize sessions. No automatic pull, push or deployment occurs.

## Preview first

Requires **Python 3.12+**. From the repository root, list baseline components without writing:

```sh
python installers/install.py hermes --dry-run
# or choose omp / codex instead of hermes
```

Native wrappers: `./installers/install.sh codex`, or `./installers/install.ps1 codex` in PowerShell.

To check a selected skill, supply the existing absolute root of the intended runtime/profile. Set `HERMES_HOME` before running this example:

```sh
./installers/install.sh hermes \
  --component proof-gated-coding-delivery \
  --destination "$HERMES_HOME" \
  --no-clobber \
  --dry-run
```

After reviewing the plan and authorizing installation, replace `--dry-run` with `--apply`.

- Writes require both `--component` and `--destination`.
- The destination is the selected runtime/profile root, outside this repository and the runtime's source checkout.
- `--no-clobber` refuses existing targets. Without a destination, local collisions cannot be checked.
- Intentional replacement without `--no-clobber` preserves the previous target in a backup; restore it manually when needed.
- Select `optional` components explicitly. Merge `manual` fragments into existing instructions yourself; the installer does not apply them.

More examples and rollback details: [portability](docs/portability.md).

## Pick your components

| Component | Targets | Adoption |
| --- | --- | --- |
| `verification` | Hermes / OMP / Codex | Reviewed instruction text; copying does not automatically load it |
| `proof-gated-coding-delivery` | Hermes / OMP / Codex | Distinguishes implementation, runtime proof and release readiness |
| `knowledge-combine` | Hermes / OMP / Codex | Optional knowledge curation; the user chooses its location |
| `handoff-template` | Hermes / OMP / Codex | Blank handoff template |
| `ecc-context-budget` / `ecc-workflow-eval` | Hermes / OMP | Selective ECC adaptations with separate offline checks |
| `personal-operator-baseline` | Hermes only | Hermes-specific operating rules |
| `hermes-soul-fragment` / `codex-agents-fragment` | Their respective runtime | Manual merge into existing instructions |
| `design-reference-loop` | Hermes / OMP / Codex | Brief → references → concepts → user choice → implementation → checks |
| 29 [design skills](design/README.md) | Hermes / OMP / Codex | Shared static Taste, Emil and Impeccable adaptations; select individually |
| `design-routing-fragment` | Hermes / OMP / Codex | Manual merge of design-skill selection rules |

All **30 design skills** live in `shared/skills` and have `optional` status. Preview the same component for any of the three runtimes:

```sh
python installers/install.py hermes --component impeccable-design --dry-run
python installers/install.py omp --component impeccable-design --dry-run
python installers/install.py codex --component impeccable-design --dry-run
```

Image generation, browsers, subagents and other capabilities come from the host. If a required tool is missing, the skill must report that limit. `prototype`, `pick-ui-library` and `review-animations` remain explicit-only in every runtime. Impeccable includes static guidance only, without its engine or hooks.

The [manifest](manifest.yaml) defines status, destinations, dependencies and `tested_on`. `reviewed` means the material was reviewed, `optional` requires explicit selection, and `manual` requires a manual merge. An empty `tested_on` does not establish runtime verification.

## Installation and agent behavior are separate checks

Tests exercise selected installs in disposable homes and compare file hashes. They do not prove discovery in an already-open chat, model adherence or quality improvement.

ECC has separately recorded discovery/read checks through OMP and Windows Hermes: [results and limitations](docs/portability.md#selective-ecc-adaptations). A fresh OMP process found the resources while an existing conversation did not adopt them. File installation and a running conversation's catalog refresh are separate events.

The optional [native ECC trial for OMP](runtimes/omp/README.md#native-ecc-trial-ecc-safe) uses a pinned Pi adapter in an isolated profile. Its PowerShell launcher keeps additional rules and lifecycle scripts disabled. This is a separate trial that preserves the normal OMP configuration.

## Continue in Codex Cloud

Create a cloud environment for `typakon4/agent-stack`, use the current `master`, and pass the context from the [Codex Cloud guide (Russian)](docs/codex-cloud.md). It includes checks, a selected-skill setup example and a ready-to-copy task handoff. Personal skills and processes from this computer do not transfer to Cloud automatically.

## Security and ownership

Previews and installs check source filenames and obvious credential signatures without printing matched values. This guard does not guarantee detection of every secret; review source and diffs manually as well.

Keep keys, browser profiles, private knowledge, raw conversations and runtime state out of this repository. An authenticated tool does not grant permission to publish, send messages, buy, delete or deploy. See [security boundaries](docs/security.md).

Jev remains an **external dependency**, pinned to `08473a5496864e8c97ee6f8f58980131ae16aed2`. Its source, MCP configuration, credentials and replay are not included. The design checker works offline; no live concept-selection adapter is connected. See [Jev integration](integrations/jev/README.md).

## Validate

```sh
python -B tests/validate_manifest.py
python -B -m unittest discover -s tests -v
python -B -m unittest discover -s design/tests -v
```

GitHub Actions runs checks on Linux and Windows with Python 3.12 and 3.14, plus native installer previews. It checks the manifest, design-skill hashes, selected installation, path boundaries, and obvious secrets in files and Git history. Tests use disposable runtime homes. Model behavior, visual quality and live Jev operation require separate evaluation.

## Add a skill or runtime

Review tool requirements, provenance, licenses and access/publication boundaries. Add the source, explicit targets and status to the manifest, then preview against the agreed destination. Preserve native policy instead of replacing whole configurations. See [architecture](docs/architecture.md).

The five baseline commits remain in history; obsolete Hermes-only files are absent from the current tree.

<sub>Cover: user-generated illustration featuring Rei Ayanami, a third-party fictional character. Unofficial; no affiliation with Evangelion or the named runtime projects. The illustration is not runtime evidence.</sub>
