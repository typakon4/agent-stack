# Skill transfer manifest

This is a curated transfer queue, not a copy of the complete local catalog. Every candidate must be scanned with SkillSpector and reviewed before it enters `skills/`.

## Include in the next transfer batch

| Source skill | Why it belongs on the Omarchy workstation |
|---|---|
| `devops/multi-host-agent-operations` | Keeps laptop/VPS boundaries safe; supports the portable baseline itself. |
| `learning/ai-engineering-tutor` | Preserves the Python-first learning workflow. |
| `creative/motion-explainer-production` | Local Remotion/video production. |
| `creative/typakon4-motion-anti-slop` | Render QA and visual-quality constraints. |
| `research/research-knowledge-workflows` | **Blocked:** SkillSpector `CRITICAL / DO_NOT_INSTALL`; it contains absorbed third-party content including an anti-refusal detection. Do not transfer unchanged. |
| `research/knowledge-combine` | Turns source collections into a curated Git-backed vault. |
| `software-development/proof-gated-coding-delivery` | Requires real artifact and execution proof for coding work. |
| `software-development/software-development-workflows` | General build, debugging, and test workflow. |
| `mcp/mcp-integrations` | Needed only when connecting a local RAG/knowledge service over MCP. |

## Keep host-specific unless there is a named use case

- VPS dashboard/Caddy, container demos, OpenWrt, Telegram signal queue, social-account automation, browser session automation, and gateway-control skills.
- Price monitors, cron/alerting, provider-specific integrations, and anything containing remote host assumptions.

## Do not transfer as a local custom skill

- Hermes built-ins and official hub skills: install/update them normally on the target machine.
- Archived skills, curator backups, security-red-team skills, raw session exports, credentials, browser data, and environment files.

## Entry gate for each candidate

```bash
~/.hermes/scripts/skillspector-scan \
  ~/.hermes/skills/<category>/<skill> \
  --format json --output /tmp/<skill>-skillspector.json
```

Include only a report-level `LOW / SAFE` result, or an explicitly reviewed exception. Record the source revision and scan report in `audits/` when copying.
