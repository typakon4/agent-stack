# Windows Hermes Desktop alongside an established Codex workstation

## Scope rule

If a user has an advanced existing Codex setup on Windows but asks to set up Hermes, split the work:

1. **Hermes Desktop introduction now** — planning, learning, vault, memory, review, and handoffs.
2. **Codex-to-Linux migration later** — separate, read-only-first portability work.

Do not install, replace, migrate, or add plugins to the existing Codex setup during the Hermes track unless the user explicitly authorizes that exact Codex surface.

## Windows facts

- Hermes Desktop and CLI share one agent/runtime, profile config, skills, sessions, and memory; Desktop is not a clone.
- Native Windows Hermes data root is `%LOCALAPPDATA%\hermes`, not `~\.hermes`.
- Use Desktop's blank/provider-later onboarding if auth, gateway, browser, and tools will be configured deliberately afterward.
- Keep an authoritative VPS Telegram gateway authoritative; do not create a second Windows gateway.

## Safe setup shape

1. Install Hermes Desktop/native Hermes.
2. Pull a secret-free Git profile distribution and install it as a named profile.
3. Authenticate Hermes locally using its own OAuth store. This does not replace the existing Codex auth/config even for the same ChatGPT account.
4. Launch Desktop against the intended vault/repository and select the named profile.
5. Keep Codex as specialised writer/tester; use Hermes Desktop for plan, research, shared memory, review, and handoffs.

## Later Codex migration: discovery requirements

Never copy `~/.codex` wholesale across OSes. Inventory and classify first:

- **Potentially portable after review:** repo-level `AGENTS.md`, reusable skills/prompts, compatible themes/keybindings, marketplace/plugin manifests.
- **Host-local:** absolute paths, sandbox/temp binaries, caches, browser profiles, OS-specific wrappers.
- **Credentials:** OAuth/auth files, API keys, cookies, SSH/Git credentials. Authenticate separately on each host.

Build a secret-free portable Codex pack only from reviewed portable items; verify in a clean Linux staging directory before altering the live laptop setup.

## Shared memory

Hindsight client configuration is credential-bearing and never belongs in Git. A new Windows host needs its own Tailnet identity and dedicated SSH key before receiving a protected local client config.