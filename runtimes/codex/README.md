# Codex mapping

`AGENTS.fragment.md` copies only the ten portable rules from the local baseline's first ten lines. It deliberately omits its machine-specific absolute `@` import. The fragment is a **manual merge**, not a replacement for existing global or project `AGENTS.md`. Project-local instructions and Codex's own safety constraints remain authoritative.

Shared skills and verification text can be previewed for an explicitly selected existing Codex runtime root. Jev, if configured for Codex, is an external **MCP** integration supplied by the runtime owner. This repo does not install Jev binaries, MCP configs, credentials, or replay. Do not duplicate an existing server registration.

The optional [design stack](../../design/README.md) includes 29 pinned static Codex adaptations under `skills/` and the shared `design-reference-loop`. Select components explicitly through the existing installer; check collisions with skills supplied by other roots/plugins too. [DESIGN.fragment.md](DESIGN.fragment.md) is a separate manual selection-policy fragment, never an AGENTS.md replacement. Its installation, runtime discovery and model adherence are distinct checks. Impeccable's executable upstream components remain excluded.
