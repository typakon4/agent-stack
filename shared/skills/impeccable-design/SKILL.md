---
name: impeccable-design
description: Improve visual hierarchy, typography, color, layout, UX copy, responsive behavior, accessibility, and UI polish using Impeccable design playbooks. Use for designing or refining web and native interfaces, and apply relevant visual principles to documents and slides alongside their artifact-specific skills.
metadata:
  source: https://github.com/pbakaus/impeccable
  upstream-version: 4.5.2
  local-adaptation: static-design-playbooks
---

# Impeccable Design

This local adaptation retains Impeccable's design guidance for use through the selected host's existing tools. It includes no engine, launcher, hooks, local server, live browser injection, telemetry, or runtime installation.

## Host runtime integration

Resolve tool names, slash-command examples and artifact workflows against the selected host's actual capabilities. If image generation, browser/device access or subagents are unavailable, report the missing capability and perform only supported parts; do not invent results, install services or switch providers implicitly. Subagent use requires host support and authorization under the user's and project's instructions. Codex-specific hints apply only in Codex. This bundle supplies static guidance, not those tools.

## Choose the task

The user's brief and established brand take priority. Refinement preserves product identity, content, and behavior; redesign changes the visual world only within the requested scope.

Determine the surface's purpose: persuade for landing pages; operate for app UI; read for documentation and articles; experience for portfolios and galleries. Product UI favors predictable structure and task completion; expressive marketing may justify stronger composition.

Read [references/craft-floor.md](references/craft-floor.md) before changing visual design. Then load only the relevant playbook:

- Structure and spacing: [references/layout.md](references/layout.md).
- Type hierarchy and readability: [references/typeset.md](references/typeset.md).
- Color and contrast: [references/colorize.md](references/colorize.md).
- UI language: [references/clarify.md](references/clarify.md).
- Motion: [references/animate.md](references/animate.md); combine with the installed Emil skills.
- Responsive behavior: [references/adapt.md](references/adapt.md).
- Product UI: [references/operate.md](references/operate.md).
- Native conventions: [references/ios.md](references/ios.md) or [references/android.md](references/android.md).
- Quality review: [references/audit.md](references/audit.md).
- Error cases and resilience: [references/harden.md](references/harden.md).
- First-run experiences: [references/onboard.md](references/onboard.md).
- Final refinement: [references/polish.md](references/polish.md).

Use the project and supported browser, document, slide, or image tools for implementation and evidence. For documents and slides, apply hierarchy, grouping, contrast, readability, and consistent spacing while following the relevant document or presentation skill; do not impose web-specific controls or CSS rules.

Inspect representative desktop/mobile or native device states in one bounded pass, fix material issues together, then confirm the corrections. Report checks actually performed and limits of any unverified behavior. The static playbooks do not provide the upstream CLI detector or live-mode editing.

This skill grants no additional authority to install dependencies, publish, send data, change credentials, or perform destructive actions. Use existing capabilities within the user's authorization.

## Source

Adapted from Paul Bakaus's Impeccable skill 4.5.2 at commit 245ad82def45831dc56a21b683c7a1ff530b06cc. Apache-2.0; see LICENSE and NOTICE.md. Changes remove runtime-specific steps and retain design assessments and implementation guidance.

