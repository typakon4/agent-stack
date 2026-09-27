# Skill transfer decisions

`manifest.yaml` is authoritative for install eligibility and target runtime. These decisions concern **copying behavior**, not turning on profiles or services. A SkillSpector LOW/SAFE report is a security gate, not proof that a skill is architecturally needed.

- **Reviewed for VPS + PC Hermes:** `personal-operator-baseline`, `ai-engineering-tutor` (Study), `knowledge-combine` (Research). Install only on a chosen profile after checking its existing instructions.
- **PC Hermes only, optional:** `motion-explainer-production`, `typakon4-motion-anti-slop`, `proof-gated-coding-delivery`, `software-development-workflows`, `mcp-integrations`. Require a real local use case; do not overwrite OMP's working skills/policies.
- **HOLD:** `multi-host-agent-operations` has a LOW/SAFE scan but assumes a central shared memory bank and old Windows Hermes paths. Review/rewrite before installation; no live-state sync.
- **BLOCKED:** `research/research-knowledge-workflows` has `CRITICAL / DO_NOT_INSTALL` in `audits/skill-transfer/research-knowledge-workflows.json`. It is not in this repository's installable `skills/`; never transfer/enable it unchanged.
- **VPS/profile-specific unless asked:** Caddy/dashboard, OpenWrt, Telegram signal queue, browser session automation, price alerts, cron/service-control and gateway operation skills. Existing Hermes bundled skills come from Hermes, not this repository.

Existing reports under `audits/` preserve source scan evidence. Re-run a skill check and review source/provenance after modifying a skill, then update the manifest deliberately. Keep credentials, host paths, raw sessions and replay state outside Git.
