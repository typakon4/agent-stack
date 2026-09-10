# Hindsight on a Tailnet with a FlClashX laptop

A concise implementation reference for a VPS-hosted Hindsight memory service shared by VPS Hermes and a local Linux Hermes.

## Service boundary

- Run Hindsight centrally on the VPS with persistent storage.
- Bind its API to the VPS Tailnet IP only, never to a public interface.
- Require an API key/tenant extension even inside the Tailnet.
- Keep Hindsight's LLM/provider key only in the VPS service configuration; each client gets a protected provider config containing only the Hindsight access credential.
- Use a named bank shared by the two Hermes profiles; do not create a separate bank just because a second host joins.

## Cost-safe starter policy

Use a bounded pilot before retaining every turn:

- one extraction request at a time;
- async retain every third turn;
- small recall context budget (for example 768 tokens);
- retain durable preferences, verified decisions, reusable procedures, and explicit handoffs only;
- use local embeddings/reranking if the VPS resources permit it.

Always run a real retain + recall test. `/health` verifies only process/database availability.

## Hindsight client setup

The Hermes Hindsight provider supports `local_external` mode. Each profile needs:

- `mode: local_external`
- a private `api_url` pointing at the Tailnet-bound Hindsight service
- an API key stored in a mode-600 profile-scoped config file
- the same `bank_id`
- `memory.provider: hindsight`

Install the Hindsight client into the same Python environment that runs the Hermes launcher. Verify with `hermes memory status` and a fresh agent session after configuration.

## FlClashX UI pattern

FlClashX is Mihomo-based and has a persistent profile-level rule editor:

1. Open **Profiles**.
2. Open the `⋮` menu on the subscribed profile.
3. Select **Override** (puzzle icon).
4. Enable the top override switch.
5. Add these rules as high-priority overrides:

| Type | Payload | Target |
|---|---|---|
| `IP-CIDR` | `100.64.0.0/10` | `DIRECT` |
| `IP-CIDR6` | `fd7a:115c:a1e0::/48` | `DIRECT` |

Enable `no-resolve` if the rule editor offers it. Save through the UI. Do not edit the subscription YAML directly because an update may overwrite it.

The override UI is for rules; it is not a raw `tun:` YAML editor. Add advanced Mihomo `route-exclude-address` settings only after direct-rule testing fails under the user's exact TUN/client version.

## Verification with FlClashX TUN enabled

- `tailscale status` shows both hosts.
- `tailscale ping <vps-tailnet-ip>` succeeds.
- `ip route get <vps-tailnet-ip>` selects `tailscale0`.
- `curl http://<vps-tailnet-ip>:<hindsight-port>/health` returns a healthy response.
- A semantic recall from the shared bank returns a fact retained from the other environment.

If mesh connectivity fails only when FlClashX TUN is active, inspect the persisted profile override and TUN strict-route settings before altering the central Hindsight service.
