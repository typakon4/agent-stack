# Portability

Use `./installers/install.sh hermes` / `omp` / `codex` to list reviewed components with no writes. On Windows use the PowerShell wrapper `./installers/install.ps1 codex`. Name an optional component explicitly to preview it. Set `HERMES_HOME` to the selected profile's existing absolute runtime root before the following commands:

```sh
./installers/install.sh hermes --component proof-gated-coding-delivery --destination "$HERMES_HOME" --dry-run
./installers/install.sh hermes --component proof-gated-coding-delivery --destination "$HERMES_HOME" --apply
```

`--apply` always needs `--component` and `--destination`; destination is an existing absolute root owned by the target runtime/profile, never this repo or the runtime's source checkout. On Windows, if the existing Codex root is under the home directory, use PowerShell's `./installers/install.ps1 codex --component proof-gated-coding-delivery --destination "$HOME\.codex" --apply`. Inspect the dry-run; the installer backs up any existing selected target before replacing it. `manual` entries cannot be installed by the helper; read and merge them locally. No automatic pull, push, host copy, or desktop/runtime installation is part of this workflow.

To add a skill: remove host paths and unsafe side effects; test its frontmatter and content; decide which runtime actually supports it; add the source, explicit relative destinations, status, dependencies, and tested runtimes to the manifest; preview each target. To add a runtime: document its policy and tool mapping, add only justified targets, and verify against that runtime rather than assuming compatibility from text alone. Keep knowledge vault destinations in that runtime's own settings, not in shared skills.
