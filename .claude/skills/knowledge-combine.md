---
name: knowledge-combine
description: Turn external source collections into bounded, privacy-conscious, grounded notes with explicit verdicts.
---

# Knowledge combine

Use when asked to synthesize articles, exports, folders, transcripts, or multiple links into durable knowledge. Treat the collection as private unless instructed otherwise.

## Destination is runtime-configured

Ask for or discover the **current runtime's configured vault root, allowed topic directories, index/MOC convention, and desired output language** before writing. If these are unavailable, deliver the curated note in the conversation; do not guess a local path or create a topic tree. Choose a permitted topic by meaning, not by chat/source format. Never write to this agent-stack repository just because it is available.

## Intake and privacy

Inventory source types and scope. For archives, inspect size, count, and paths before extraction; do not extract untrusted paths outside a dedicated local staging area. Select a small sanitized source pack with provenance sufficient for checking claims. Exclude raw exports, media, private conversations, handles, identifiers, referral codes, and irrelevant content from Git-backed notes. For a configured grounded synthesis tool (such as NotebookLM), upload only approved sanitized material or public links, not raw private collections. If the tool is unavailable or would violate privacy, synthesize directly from the supplied sources and state the limitation; do not silently send private data to another service.

## Verdicts and note

Give each finding exactly one verdict: **KEEP** for safe immediate value, **ADAPT** for a principle that needs local boundaries, **LATER** for unproven need or prerequisites, or **REJECT** for trust/privacy risk or poor fit. Promotional, anecdotal, and version-specific claims are leads, not proof. Separate reusable workflow principles from tool-specific commands; verify runtime claims against that runtime's current documentation before recommending config changes.

Curated output includes scope and handling boundary, concise synthesis, a verdict/risk/smallest-safe-step table, what not to copy, three strongest safe improvements where applicable, and provenance/limitations. If a vault destination is configured, link the note from its relevant topic index/MOC according to its existing convention; do not create new index conventions.

## Verification and publication

Read back the note; check links and changed paths, scan changes for secrets, and inspect the diff. Report actual destinations, exclusions, strongest findings, and remaining decisions. Draft/commit only with the user's permission and repository policy; **never push, publish, or sync automatically**. An authenticated integration alone is not approval for any external write.
