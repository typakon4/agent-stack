# Secret-free portable Hermes synchronization

Use when carrying a Hermes workflow between a VPS and workstation without cloning machine state.

## Boundary

Synchronize only a Git-backed profile distribution: skills, portable config, operating docs, and reviewed marketplace artifacts. Keep OAuth, `.env`, browser state, SSH keys, sessions, service tokens, proxy settings, and remote-memory credentials local to each host.

## Update flow

On the workstation, update the baseline checkout and then the recorded profile source:

```bash
cd ~/Projects/ai-learning-vault
git pull --ff-only
hermes profile update <profile-name> --yes
hermes -p <profile-name> skills list
hermes -p <profile-name> memory status
```

Do not add `--force-config` unless the user explicitly requests overwriting local configuration: ordinary profile update preserves `config.yaml`, auth, `.env`, sessions, and memories.

## Shared memory

When Hindsight is centralized on the VPS, do not copy memory files between hosts. Each device needs its own authorized, private connection configuration; verify it with `hermes -p <profile-name> memory status`. Treat the central memory service as a connection target, not a Git artifact.

## Skill intake before propagation

Audit newly added or materially changed skills before placing them in the portable distribution. In a SkillSpector JSON report, use `risk_assessment.severity` and `risk_assessment.recommendation` as the package verdict. Do not classify a package by the strongest severity word anywhere in its issue text: a local heuristic issue may be MEDIUM while the package verdict is `LOW / SAFE`.

Do not propagate a stale baseline copy when the current upstream version is `HIGH` or `CRITICAL`; remove it from the portable distribution pending review.

## Provider-network troubleshooting boundary

A successful `curl` TLS connection to `chatgpt.com` only proves DNS/TCP/TLS reachability. It does not prove that an authenticated streaming Codex request will pass Cloudflare. Do not repeatedly reauthenticate until the provider log distinguishes an OAuth error from a proxy/Cloudflare streaming block.
