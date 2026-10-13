# agent-stack

Portable agent behavior stack for Hermes, OMP, and Codex.

## Project context

This repository contains reviewed skills and instructions for AI agents. The stack includes:

- **Skills**: Modular behaviors for context auditing, workflow evaluation, knowledge synthesis, and proof-gated delivery
- **Instructions**: Verification guidelines and handoff templates
- **Installers**: Safe deployment scripts with dry-run support
- **Integrations**: Jev external MCP layer

## Working conventions

- Python 3.12+ for validation and tests
- Git history includes provenance commits
- Never auto-push, auto-deploy, or sync without explicit approval
- Keep credentials, tokens, and secrets local to their host
- Use disposable fixtures for testing, never real user data

## Key components

- `shared/skills/` — Cross-runtime reviewed skills
- `runtimes/` — Runtime-specific mappings (hermes/omp/codex)
- `installers/` — Safe installation with containment checks
- `tests/` — Manifest validation and installer regression tests

## Development workflow

1. Read existing patterns before adding new components
2. Test changes with `python tests/validate_manifest.py`
3. Run installer dry-runs before applying
4. Verify no secrets entered portable material
5. Commit only when explicitly authorized

## Security boundaries

- No automatic external writes (push, publish, deploy)
- Credentials stay local to their profile/host
- Installer rejects obvious secrets before any file operation
- Manual review required for SOUL/AGENTS fragments
