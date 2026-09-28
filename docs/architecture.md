# Architecture

`manifest.yaml` lists reviewed/optional/manual components with a source path and an explicit relative target for each supported runtime. `shared/` holds runtime-neutral skills, instructions, and a blank handoff template. `runtimes/hermes/` holds a Hermes-specific operator skill and a manual SOUL fragment; `runtimes/omp/` and `runtimes/codex/` explain how shared material fits existing local policy. `integrations/jev/` records an external Jev dependency, not an integration install.

`installers/` previews by default and only installs a named eligible component into an explicitly supplied, existing, absolute runtime root with `--apply`. Selection is per component and runtime; no whole-config replacement, automatic host sync, or upgrade of Hermes/OMP/Codex/Jev. The runtime owns executables, configuration, identity, models, skills outside this manifest, and state. A shared skill may describe a process but never provide authorization for external side effects.
