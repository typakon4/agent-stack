---
name: context-budget
description: Use when auditing context pressure, skill/tool overhead, or headroom before adding agent components; read-only recommendations, not configuration changes.
---

# Selective context budget

Adapted from Affaan Mustafa's ECC context-budget (MIT). This is a portable rewrite.

## Boundaries

- Preserve existing instructions and memory. Do not replace memory or alter settings, models, auth, tools, skills, or MCP configuration.
- Inspect only public skill/instruction metadata and explicitly selected non-sensitive content. Never read auth files, environment files, raw transcripts, session stores, or logs.
- Report aggregate counts and measurements, not raw prompts, tool schemas, chats, private filenames, or memory. Recommendations grant no permission to disable or rewrite anything.

## Run a bounded audit

1. **Set scope:** identify the runtime/version, current task, and selected catalog roots. Discover the selected profile's runtime home rather than assuming a path.
2. **Separate three kinds of evidence:**
   - **On-disk catalog:** installed counts, duplicate bodies, file bytes, and short description sizes. A file's presence does not prove its body is in the model context.
   - **Active context:** only the instructions, descriptions, loaded bodies, tool schemas, history, and other content the harness actually reports as included.
   - **Usage:** the harness's input/output/cache/reasoning token counters for the stated turn or run.
3. **Measure narrowly:** prefer actual harness-reported context tokens and capacity with their timestamp/scope. If both describe the same active window, compute `headroom = capacity - occupied`.
4. **Inventory the selected catalog:** list metadata, count files and bytes, and identify identical content locally without printing it. Report physical copies separately from unique content.
5. **Label estimates:** if no actual token count exists, retain byte counts. An optional text estimate such as `characters / 4` must state the formula, counted scope, and uncertainty.
6. **Recommend at most three actions:** tie each to observed loaded overhead or a clearly labeled inference. Favor narrower retrieval, shorter duplicated instructions, and on-demand loading.

## Report

Use a short table with columns `scope | count/bytes | actual tokens | estimate/method | evidence`. Write `unmeasured` for missing fields.

Then state:

- Runtime/profile label and measurement scope; actual active tokens/capacity/headroom if available.
- Catalog copies versus unique bodies; these are disk facts, not active-context totals.
- Up to three recommendations with measured savings, or `savings unmeasured` and the reason.
- What was not inspected or changed, and whether the loaded inventory is known or inferred.
