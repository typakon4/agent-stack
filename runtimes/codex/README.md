# Codex mapping

`AGENTS.fragment.md` copies only the ten portable rules from the local baseline's first ten lines. It deliberately omits its machine-specific absolute `@` import. The fragment is a **manual merge**, not a replacement for existing global or project `AGENTS.md`. Project-local instructions and Codex's own safety constraints remain authoritative.

Shared skills and verification text can be previewed for an explicitly selected existing Codex runtime root. Jev, if configured for Codex, is an external **MCP** integration supplied by the runtime owner. This repo does not install Jev binaries, MCP configs, credentials, or replay. Do not duplicate an existing server registration.

The optional [design stack](../../design/README.md) includes 30 common skills under `shared/skills`, available for Hermes/OMP/Codex. Select components explicitly through the existing installer; check collisions with skills supplied by other roots/plugins too. [Shared design routing](../../shared/instructions/design-routing.md) is a manual selection-policy fragment, never an AGENTS.md replacement. File installation, runtime discovery and model adherence are distinct checks. Impeccable's executable upstream components remain excluded. For a new cloud task, see the [Russian Codex Cloud guide](../../docs/codex-cloud.md).
