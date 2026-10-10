---
name: ecc-context-budget
description: Use when auditing context pressure, skill/tool overhead, or headroom before adding agent components; read-only recommendations, not configuration changes.
license: MIT
---

# Selective context budget

Adapted from Affaan Mustafa's [ECC context-budget](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/context-budget/SKILL.md), commit `ef648e01899ba3e8dc6371642deaaf64b4477775` (MIT; notice in `LICENSE`). This is a portable rewrite, not ECC installation or a new always-loaded policy.

## Boundaries

- Preserve Ponytail, proof-gated delivery, Jev routing, Mnemopi, and the host's existing instructions. Do not replace memory or alter settings, models, auth, tools, skills, or MCP configuration.
- Inspect only public skill/instruction metadata and explicitly selected non-sensitive content. Never read auth files, environment files, raw transcripts, session stores, or logs. If needed, request only a named non-secret setting through the host's narrow accessor; do not dump a config.
- Report aggregate counts and measurements, not raw prompts, tool schemas, chats, private filenames, user paths, or memory. Recommendations grant no permission to disable or rewrite anything.

## Run a bounded audit

1. **Set scope:** identify the runtime/version, current task, and selected catalog roots. Use the host's supported skill catalog/loader and current-session status or usage surface; discover the selected profile's runtime home rather than assuming a path. OMP can load a skill through `omp read skill://NAME`; Hermes exposes `skills_list()` and `skill_view(NAME)`. These are loader operations, not context meters. Do not start a paid model call just to collect metrics.
2. **Separate three kinds of evidence:**
   - **On-disk catalog:** installed counts, duplicate bodies, file bytes, and short description sizes. A file's presence does not prove its body is in the model context.
   - **Active context:** only the instructions, descriptions, loaded bodies, tool schemas, history, and other content the harness actually reports as included. Catalog descriptions may be included while bodies are loaded on demand; check the runtime rather than assuming this.
   - **Usage:** the harness's input/output/cache/reasoning token counters for the stated turn or run. Cumulative billed input is not necessarily the current occupied window; cache hits do not remove active context.
3. **Measure narrowly:** prefer actual harness-reported context tokens and capacity with their timestamp/scope. If both describe the same active window, compute `headroom = capacity - occupied` and flag an inconsistent negative value instead of silently clamping it. Otherwise mark headroom `unmeasured`. Never subtract the entire disk catalog from the context limit.
4. **Inventory the selected catalog:** list metadata, count files and bytes, and identify identical content locally without printing it. Report physical copies separately from unique content. Deduplication on disk does not prove the runtime deduplicates active context. Count public description sizes separately from skill bodies; exclude license/support files from body totals.
5. **Label estimates:** if no actual token count exists, retain byte counts. An optional text estimate such as `characters / 4` must state the formula, counted scope, and uncertainty; it is not a token measurement, a billing figure, or measured headroom. Do not assign a fixed token cost per tool, assume a model window, or invent savings.
6. **Recommend at most three actions:** tie each to observed loaded overhead or a clearly labeled inference. Favor narrower retrieval, shorter duplicated instructions, and on-demand loading. Keep existing safety/verification/memory policies. Propose configuration changes for separate review; do not perform them. If continuing needs a handoff, use the existing `shared/templates/handoff.md` contract and reviewed facts only, never a transcript dump.

## Report

Use a short table with columns `scope | count/bytes | actual tokens | estimate/method | evidence`. Write `unmeasured` for missing fields.

Then state:

- Runtime/profile label and measurement scope; actual active tokens/capacity/headroom if available.
- Catalog copies versus unique bodies; these are disk facts, not active-context totals.
- Up to three recommendations with measured savings, or `savings unmeasured` and the reason.
- What was not inspected or changed, and whether the loaded inventory is known or inferred.

## Safe smoke workflow

Select only this skill and `ecc-workflow-eval` in the approved runtime catalog. Load their metadata/bodies through the supported loader, measure their source file bytes without printing private content, and report the two catalog entries separately from active context. With no active-session context meter, the correct active-token/headroom result is `unmeasured`, not a guessed percentage. This checks catalog access and honest accounting; it does not test model adherence or prove token savings.
