---
name: local-agent-backed-apps
description: Integrate web/apps with a local authenticated agent CLI (Hermes/Codex) as a server-side model backend instead of requiring app-level API keys.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [ai-integration, hermes, codex, nextjs, api-keys, server-side]
    related_skills: [hermes-agent, github-repo-management]
---

# Local Agent-Backed App Integrations

Use this when a project needs model calls but the user does **not** want to put provider API keys into the app. The class of solution is: keep model access on the server, call a locally authenticated agent/CLI such as Hermes with Codex OAuth, validate strict output, and expose only the app's own API route to the browser.

## Trigger conditions

- User says they want model connection "through Codex", "through you/Hermes", or "without API keys".
- A web app currently reads `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc. directly for a feature.
- The app is server-rendered / has backend routes (Next.js App Router, Express, FastAPI, etc.) and can safely run a local CLI on the server.

## Core pattern

1. **Inspect current model boundary**
   - Find where the app calls the provider API.
   - Confirm it is server-side only. If provider calls happen in client code, move them behind a server API route first.

2. **Add a provider switch**
   - Prefer explicit env selection:
     ```env
     FOOD_PARSER_PROVIDER="hermes"
     HERMES_FOOD_COMMAND="hermes"
     HERMES_FOOD_PROVIDER="openai-codex"
     HERMES_FOOD_MODEL="gpt-5.4"
     ```
   - Keep direct API mode as optional, not default, when useful:
     ```env
     FOOD_PARSER_PROVIDER="openai"
     OPENAI_API_KEY=""
     OPENAI_FOOD_MODEL="gpt-4o-mini"
     ```

3. **Call the local agent from server code only**
   - Use `execFile`/argument arrays rather than shell interpolation.
   - Include timeout and maxBuffer.
   - Set `NO_COLOR=1` to reduce noisy terminal formatting.
   - Example shape:
     ```ts
     const { stdout, stderr } = await execFileAsync(
       "hermes",
       [
         "chat",
         "--quiet",
         "--provider",
         "openai-codex",
         "--model",
         "gpt-5.4",
         "--query",
         prompt,
       ],
       { timeout: 120_000, maxBuffer: 1024 * 1024, env: { ...process.env, NO_COLOR: "1" } },
     );
     ```

4. **Constrain and validate output**
   - Ask for JSON only, no Markdown fences.
   - Pass or describe the exact JSON schema.
   - Still defensively extract JSON from stdout because CLIs may include wrappers.
   - Validate with the app's schema layer (Zod/Pydantic/etc.) before returning to the UI.

5. **Document deployment assumptions**
   - This only works on a host where the local agent CLI is installed and authenticated.
   - The browser never receives provider credentials.
   - The app still needs normal server runtime permissions to spawn the CLI.

6. **Verify before committing**
   - Run the project's lint/typecheck/build commands.
   - Check `git diff` to ensure no accidental lockfile churn or secret exposure.
   - If `npm install` rewrites `package-lock.json` without dependency changes, consider reverting lockfile noise before commit.

## Pitfalls

- **Do not add API keys to client env vars.** In Next.js, anything `NEXT_PUBLIC_*` is browser-visible.
- **Do not silently enable paid fallbacks.** This user is cost-sensitive; direct API fallback should be opt-in and documented.
- **Do not use shell strings for user-provided text.** Use `execFile` args to avoid injection issues.
- **Expect local CLI latency.** Calling a full agent is slower than direct model API calls. Use it for development, personal/self-hosted apps, demos, or low-volume workflows unless a queue/cache is added.
- **Keep structured output strict.** The agent may return explanatory text unless explicitly constrained and post-validated.

## References

- `references/fitness-hermes-codex-parser.md` — concrete Next.js food parser conversion from OpenAI API key to local Hermes/Codex CLI provider.
