---
name: multi-host-agent-operations
description: "Set up and operate one personal AI agent across a VPS and local workstation: portable profiles, safe identity/config synchronization, central shared memory, private mesh networking, and coexistence with local proxy/VPN clients."
version: 1.0.0
---

# Multi-Host Agent Operations

Use when a user wants a VPS-based agent and a local workstation agent to feel continuous without copying credentials, raw sessions, or an entire home directory.

## Core model

Separate state by safety boundary:

| Shared deliberately | Local to each host |
|---|---|
| Identity/SOUL, approved skills, safe config templates, durable handoffs, central memory bank | OAuth/API credentials, SSH/Git keys, browser profiles/cookies, raw sessions/state DB, machine paths, files, gateways |

Do **not** use bidirectional sync/rsync of the full agent home. It creates secret exposure, state conflicts, and duplicate messaging gateways.

## Temporary colocated VPS demos

When the user explicitly wants a short-lived demo on an existing VPS rather than a durable production service, do **not** automatically create a new Linux service account, persistent identity layer, or full production operating model. Keep the current operator account and isolate the demo through:

- a distinct project directory and Compose project name;
- dedicated named volumes and an untracked environment file;
- a separate Caddy site that does not alter existing routes;
- a documented teardown path.

Before adding a Caddy site or requesting TLS, verify that the exact temporary hostname resolves publicly to the target VPS. Treat DNS propagation and a deployable source branch/artifact as prerequisites. This exception is for explicitly temporary demos only; do not apply it to a long-lived public service without revisiting account isolation, backups, and access control.

## Implementation sequence

1. **Discover surfaces before editing.** Identify the VPS agent profile, the target local OS/device, existing VPN/proxy stack, desired model auth, and whether the user wants a messaging gateway locally. Do not infer a local gateway from an existing VPS Telegram gateway.
2. **Bootstrap the portable core, then inventory skills.** First package only secret-free `SOUL.md`, safe config defaults, and a handoff template so the fresh host has a usable baseline. Then generate a human-readable manifest from every active, non-archived global skill plus any relevant profile-scoped skills. For each exact slug, show `included` or `excluded`, a short description, audit verdict, and whether it is global, portable-only, or VPS/profile-only. Transfer reviewed skills in small batches; do not clone a large local catalog wholesale. Explicitly ask the user to select additions when the desired laptop scope is ambiguous. Do not silently fold gateway/cron-specific profiles (for example, a Signal Queue) into a general local profile.
3. **Interpret skill scans correctly.** For SkillSpector, use the report-level `risk_assessment.severity` and `recommendation` as the decision. Do **not** classify a skill by the highest severity of an individual heuristic finding; a `LOW / SAFE` report can contain a contextual MEDIUM finding. Preserve the raw report outside the portable pack and record the final inclusion decision.
4. **Package a portable distribution.** Put only secret-free `SOUL.md`, safe config defaults, reviewed skills, and handoff templates in a Git-backed distribution. Validate it in an isolated agent home before publishing. Keep credentials, memories, and sessions out of Git.
5. **Install locally as a separate profile.** Use the distribution rather than cloning the VPS home. Authenticate the model provider locally. Do not copy OAuth tokens.
4. **Join private mesh networking.** Use a private overlay such as Tailscale for host-to-host services. Bind central internal services to the mesh address only; do not expose them through a public IP merely for laptop access.
5. **Add central memory only after its service, model, retention, and cost policy are explicit.** Configure both profiles to use the same named bank. Give each host its own protected provider client config; transfer any bootstrap secret over SSH/Tailscale, never Git or chat.
6. **Verify end-to-end.** A health endpoint is insufficient: retain one non-secret durable fact, recall it semantically, verify each client has the active provider, then test a fresh agent session.
7. **Establish update/handoff flow.** Git updates the portable baseline. The central memory stores durable semantic knowledge. Versioned handoff files carry proof, active project state, and next actions.

## Shared memory guardrails

- Make retention frequency, recall budget, model/provider, and concurrency explicit before enabling auto-retain.
- Retain only durable preferences, verified decisions, reusable procedures, and explicit handoffs.
- Never retain secrets, OAuth data, raw environment files, cookies, or private keys.
- Built-in local memory remains host-scoped; a central provider is the shared durable layer.
- Prefer one named bank for one user/operator, not one bank per device.
- Choose the context layer by retrieval need before deploying RAG. Built-in memory covers compact preferences; a shared memory provider covers cross-host semantic continuity; a separate knowledge brain/vector stack is justified only for searchable document corpora. See `references/knowledge-context-architecture.md`.

## Private live browser access over Tailscale

When a persistent VPS browser needs a human-only login or verification step, expose its **viewing/control surface only on the Tailnet**, not through a public reverse-proxy route. This lets the user operate a browser that remains on the VPS without keeping a laptop powered on.

1. Confirm Tailscale is installed, authenticated into the intended Tailnet, and obtain the VPS Tailnet IPv4 / MagicDNS name plus the user's online device.
2. Keep browser-control and raw VNC endpoints loopback-only. Bind only the noVNC web UI to the VPS Tailnet address (for example `100.x.y.z:6080`), never `0.0.0.0`.
3. Test the noVNC HTTP page on the Tailnet address and `tailscale ping` the user's device. Confirm the raw VNC port is still only `127.0.0.1` / `::1` and the public listener is absent.
4. Give the user the Tailnet URL (for example `http://<tailnet-ip>:6080/vnc.html?autoconnect=true&resize=scale`) and keep a real, visible browser tab open before asking them to log in.
5. Remove any temporary public Caddy/noVNC route after the Tailnet path is verified. Do not expose an unauthenticated browser-control API, VNC, or noVNC on the public IP.

For bot-protected sites, do not construct proxy/fingerprint schemes to defeat challenges. Prefer an existing user-authorized authenticated session, an official API, or a one-time user login in the persistent VPS browser. If the user supplies a cookie export for their own account, treat it as a secret and follow the authenticated-session workflow; state honestly that provider clearance may be IP/device-bound and must be tested.

### VNC service pitfalls

- A noVNC watcher running as an unprivileged service user must log to a writable directory such as `${TMPDIR:-/tmp}`, not `/var/log`.
- Ensure x11vnc itself uses `-localhost`; a noVNC bind setting does **not** automatically restrict the raw VNC listener.
- Verify the full interactive path, including WebSocket connection and a visible browser tab—not just `GET /vnc.html` returning 200.
- noVNC mouse/keyboard input does not count as Camofox tool activity. Set explicit long `TAB_INACTIVITY_MS`, `SESSION_TIMEOUT_MS`, and `BROWSER_IDLE_TIMEOUT_MS` values for a human-operated live browser, or the default reaper can make it appear to reload repeatedly.

For a concrete persistent Camofox/noVNC systemd configuration and verification checklist, see `references/camofox-vnc-tailnet.md`.

## Networking and full-tunnel proxy/VPN coexistence

A mesh overlay is not necessarily the user's public-internet VPN. A commercial VPN, WireGuard tunnel, or Clash/Mihomo TUN may coexist with the mesh, but must not capture or block mesh routes.

1. First identify the actual client/control surface. For GUI clients, give UI-first instructions before raw YAML.
2. For Mihomo/Clash-style clients, add high-priority `DIRECT` rules for the mesh IPv4/IPv6 CIDRs in the profile's persistent override mechanism. Do not edit a subscription file that updates will overwrite.
3. Test mesh ping, route selection, and the private service health endpoint while the proxy TUN is enabled.
4. Only if direct rules do not work, add advanced TUN route exclusions; document the exact client/version and back up the profile first.
5. Do not use a Tailscale exit node concurrently with another full-tunnel VPN unless the routing design has been explicitly verified.

See `references/hindsight-tailnet-flclash.md` for a concrete Hindsight + Tailscale + FlClashX pattern.

## Windows Hermes Desktop beside an existing Codex setup

When the target workstation is a Windows PC with an established Codex environment, explicitly separate the two surfaces before changing anything. Adding Hermes Desktop must not silently become a Codex migration, plugin installation, OAuth overwrite, or `~/.codex` clone.

1. Add Hermes through the native Windows Desktop/CLI path and install the secret-free profile distribution.
2. On Desktop onboarding, use the blank/provider-later path when provider, gateway, browser, and tools need deliberate configuration.
3. Authenticate Hermes locally; its OAuth store is separate from existing Codex auth even when both use the same ChatGPT account.
4. Use Hermes Desktop as the visual planning, learning, vault, memory, and review layer; keep the user's existing Codex as the specialised implementation/test layer.
5. Schedule Codex-to-Linux migration as a later read-only-first task. Inventory portable rules/skills separately from host-local caches/paths and credentials; never copy a complete `.codex` directory across OSes.

Native Windows Hermes data lives under `%LOCALAPPDATA%\\hermes`, not `~\\.hermes`. A Windows host joining shared Hindsight needs its own Tailnet identity and SSH key; the credential-bearing client config stays local and out of Git.

See `references/windows-hermes-desktop-codex-coexistence.md` for the operating sequence and portability boundaries.

## Hermes-specific operational checks

- A local workstation profile normally has no Telegram gateway when VPS Telegram is authoritative.
- Profile/model changes apply on a fresh session; gateway config needs a gateway restart.
- When restarting a gateway from its own active session is unsafe, use the authenticated dashboard's restart flow and let it drain active agents; do not force-kill the process.
- For Hermes Desktop remote gateway over Tailscale, `127.0.0.1:9119` on the workstation means the workstation itself, not the VPS. Use the VPS Tailnet URL (`http://<tailscale-ip>:9119` or MagicDNS) in **Settings → Gateway → Remote gateway**.
- `/api/status` confirms service reachability and advertised providers, but it does **not** prove the Desktop password form works. Verify the real `POST /auth/password-login` flow exactly once after credential changes, including JSON `provider: "basic"`, username, and password; it is rate-limited by client IP.
- When rotating basic auth, deliberately set both `HERMES_DASHBOARD_BASIC_AUTH_USERNAME` and `HERMES_DASHBOARD_BASIC_AUTH_PASSWORD`, preserve `HERMES_DASHBOARD_BASIC_AUTH_SECRET`, restart only `hermes-serve`, then validate the actual form login. A stale username otherwise appears as an opaque `401 Invalid credentials` in Desktop.
- Confirm distribution install, local model auth, memory provider availability, private network reachability, retain/recall, and a fresh-session recall before calling the setup complete.

## Reporting

Report what is shared vs intentionally isolated, exact active service exposure, retention/cost settings, and actual verification results. Do not claim that two agents have "one memory" until both clients have passed recall against the same bank.
