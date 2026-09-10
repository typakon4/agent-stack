# Telegram ZIP and YouTube combine — operational reference

Use this reference when the source batch includes Telegram HTML/ZIP exports, YouTube links, or both.

## Telegram HTML/ZIP

1. Inspect archive safely before extraction: entry count, compressed/uncompressed size, root files.
2. Locate `messages.html`; extract only message text and metadata needed for inventory.
3. Create a **local-only** inventory and select relevant candidates by semantic topic.
4. Exclude raw ZIPs, photos, stickers, media, handles, referral codes, private correspondence, and unrelated personal posts from vault/Git.
5. Make a bounded sanitized Markdown candidate pack. Preserve enough title/date/source provenance for grounded synthesis, but avoid identities where unnecessary.
6. Upload the sanitized pack to NotebookLM through the `gemini-pro` profile. Do not upload the full export unless the user explicitly asks and privacy scope is confirmed.

## YouTube batches

1. Fetch titles/metadata first to establish topic routing.
2. Create a dedicated NotebookLM notebook and add YouTube URLs directly as sources when supported.
3. Wait until every source is ready before asking the synthesis question.
4. Prompt for:
   - claim map per video;
   - duplication versus unique material;
   - evidence/detail versus marketing or version-specific demo claims;
   - verdicts, boundaries, and minimum safe next steps.
5. Store NotebookLM’s raw answer under `topics/<topic>/raw/youtube/` only when it contains no personal/private data. Label it raw synthesis and explicitly say it is not an authority on current Hermes behavior.

## Hermes-specific reality check

Video/community material often presents old paths, commands, or features as current. Treat it as a source of patterns, not an operational specification. Before curating a Hermes recommendation:

- consult current official Hermes documentation;
- identify whether the claim is a reusable principle or an implementation detail;
- keep the principle as **АДАПТИРОВАТЬ** if appropriate;
- never make config, skills, plugin, memory, cron, model/provider, or runtime changes as part of intake.

## Curated artifact shape

- Write the curated note in Russian; retain English product names and identifiers only where they improve findability.
- Use Russian verdict labels in the note: **СОХРАНИТЬ / АДАПТИРОВАТЬ / ПОЗЖЕ / ОТКЛОНИТЬ**. If an external prompt required English labels, give both once in a legend.
- Include source links, method, synthesis, verdict table, anti-patterns, limitations, and three safe improvements.
- Link the note from the topic index and MOC.
- Verify wikilinks, whitespace, secret patterns, diff, then commit/push.

## Practical anti-patterns observed

- Treating raw channel exports as vault material.
- Copying remote public MCPs, agent networks, unofficial API routers, or public ZIP deployment patterns into private workflows.
- Adding Vector DB/RAG, local LLM-Ops, cron automation, or OS migrations before a measured need exists.
- Treating “self-improving” claims as permission for silent persistent changes.
