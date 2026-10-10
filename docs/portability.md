# Portability

Use `./installers/install.sh hermes` / `omp` / `codex` to list reviewed components with no writes. On Windows use the PowerShell wrapper `./installers/install.ps1 codex`. Name an optional component explicitly to preview it. Set `HERMES_HOME` to the selected profile's existing absolute runtime root before the following commands:

```sh
./installers/install.sh hermes --component proof-gated-coding-delivery --destination "$HERMES_HOME" --dry-run
./installers/install.sh hermes --component proof-gated-coding-delivery --destination "$HERMES_HOME" --apply
```

`--apply` always needs `--component` and `--destination`; destination is an existing absolute root owned by the target runtime/profile, never this repo or the runtime's source checkout. On Windows, if the existing Codex root is under the home directory, use PowerShell's `./installers/install.ps1 codex --component proof-gated-coding-delivery --destination "$HOME\.codex" --apply`. Inspect the dry-run; the installer backs up any existing selected target before replacing it. `manual` entries cannot be installed by the helper; read and merge them locally. No automatic pull, push, host copy, or desktop/runtime installation is part of this workflow.

Add `--no-clobber` to both preview and apply when adopting a new component. With `--destination`, every selected target is checked before writes: any existing target refuses the whole selection. Without that flag, an intentional replacement retains the previous target under `.agent-stack-backups/`; restore it manually after reviewing the backup. A dry-run without a destination lists components but cannot check local collisions. Source filename/content checks also run before any writes; diagnostic messages name the file and signature type, never the matched credential.

To add a skill: remove host paths and unsafe side effects; test its frontmatter and content; decide which runtime actually supports it; add the source, explicit relative destinations, status, dependencies, and tested runtimes to the manifest; preview each target. To add a runtime: document its policy and tool mapping, add only justified targets, and verify against that runtime rather than assuming compatibility from text alone. Keep knowledge vault destinations in that runtime's own settings, not in shared skills.

## Selective ECC adaptations

`ecc-context-budget` and `ecc-workflow-eval` are optional, explicitly selected skills for OMP and Hermes only. They are concise rewrites credited to Affaan Mustafa's ECC, pinned to `ef648e01899ba3e8dc6371642deaaf64b4477775`; each installed directory includes the upstream MIT notice. No ECC package, hooks, framework, or default policy is installed. Existing Ponytail/proof/Jev/Mnemopi and handoff instructions retain their authority.

Preview each runtime with `--component ecc-context-budget --component ecc-workflow-eval --no-clobber` and its existing absolute `--destination`; add `--apply` only for the reviewed targets. Check for name collisions in the actual catalog too: `--no-clobber` refuses existing destination files/directories, but cannot discover a same-named skill supplied by a plugin or another search root. The existing installer otherwise supports intentional replacement/backups.

Choose OMP's actual agent/profile root, not a plugin dependency's `.pi` root. Choose Hermes's actual profile home: on Windows its platform default is `%LOCALAPPDATA%\hermes`, not `~/.hermes`, and a profile or `HERMES_HOME` override can select another root. Do not use the Hermes source checkout as the destination or dump settings/auth to discover it.

### Load on demand

- Fresh OMP CLI discovery: `omp skill list --json`. Body reads: `omp read skill://ecc-context-budget` and `omp read skill://ecc-workflow-eval`.
- Hermes's actual skill tools: `skills_list()` then `skill_view(name="ecc-context-budget")` or `skill_view(name="ecc-workflow-eval")`.
- In a new session, ask: “Use ecc-context-budget to audit the selected skill catalog and distinguish it from measured active context” or “Use ecc-workflow-eval to compare the same small behavioral tasks before and after this authorized change.” These are natural-language triggers, not invented slash commands.

File installation and fresh CLI/tool discovery do **not** prove an already-running conversation adopted a new catalog. The current OMP host still rejected `skill://ecc-context-budget` after installation while its fresh CLI loaded it successfully. Start a new session and verify availability; automatic hot reload and a supported reload command were not proved. Long-lived Hermes conversations likewise were not tested for adoption. Listing loads metadata, not every skill body; loaded bodies and actual active-window tokens are different observations.

### Exercised local proof — 2026-10-06

OMP 18.6.0 and Windows Hermes `0.21.5+5805.g54bc5e5` were exercised through their actual offline surfaces, not the unrelated pi SDK. Source review found no blocking issue. Explicit dry-run/apply installed only the two selected skill directories into the existing local runtime roots; no collision existed. Installed `SKILL.md` and `LICENSE` bytes matched their reviewed sources.

| Fixed task | Before | After |
|---|---|---|
| OMP existing proof skill body read | PASS | PASS |
| OMP new context skill body read | FAIL: not yet installed | PASS |
| OMP new eval skill body read | FAIL: not yet installed | PASS |
| OMP selected-target dry-run leaves destination unchanged | PASS | PASS |
| Hermes selected-target dry-run leaves destination unchanged | PASS | PASS |

First-attempt observations: 3/5 before, 5/5 after, zero corrections. The two intended pre-install capability failures are not regressions or statistical reliability estimates. Matched tasks used the same repository working directory; catalog comparisons additionally used the independent baseline's exact temporary working directory and default profile.

Fresh OMP discovery returned 12→14 entries, both new entries non-hidden at the intended native paths, no discovery warnings. Guarded actual Hermes discovery returned 51→53 entries; `skill_view(name, preprocess=False)` returned both bodies from the intended runtime root. The Hermes probe used the already-committed managed dependency import path, not bootstrap/pip; its audit guard denied secret reads, writes, network and subprocess launches. Two loader warning lines were counted without dumping them.

Context-accounting smoke: two unique selected bodies total 10,484 on-disk UTF-8 bytes, installed as four physical runtime copies. Body bytes exclude license notices. Active tokens, capacity, headroom, input/output/cache/reasoning usage, USD and token savings were **unmeasured**. Hermes compact catalog metadata grew 4,956→5,372 bytes; OMP returned 4,577→4,758 bytes, but existing descriptions also differed by 235 bytes, so its total delta is confounded. Catalog bytes are not active context or billing.

Checks measured command/startup wall time, not model performance; no paid model calls occurred. Model adherence, quality improvement, hot reload, and other runtime/platform support remain untested. The eval workflow was exercised as this fixed deterministic loader/dry-run comparison, not a source-text grader or prose-pinning test.
