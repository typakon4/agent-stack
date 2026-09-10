# Fitness repo: OpenAI API key -> local Hermes/Codex parser

Session pattern captured from `typakon4/fitness`, a Next.js Fitness RPG app with `/api/food/parse`.

## Starting point

- Server parser lived in `src/lib/food-parser/parser.ts`.
- It required:
  ```env
  OPENAI_API_KEY=""
  OPENAI_FOOD_MODEL="gpt-4o-mini"
  ```
- Route `/api/food/parse` called `parseFoodText`, which used OpenAI Responses API with a strict JSON schema and Zod validation.

## Desired outcome

The user wanted model access through Codex/Hermes, not through an app API key.

## Conversion shape

Add env-controlled provider routing:

```ts
const FOOD_PARSER_PROVIDER = (process.env.FOOD_PARSER_PROVIDER ?? "hermes").toLowerCase();
const DEFAULT_OPENAI_MODEL = process.env.OPENAI_FOOD_MODEL ?? "gpt-4o-mini";
const DEFAULT_HERMES_MODEL = process.env.HERMES_FOOD_MODEL ?? "gpt-5.4";
const DEFAULT_HERMES_PROVIDER = process.env.HERMES_FOOD_PROVIDER ?? "openai-codex";
```

Default path:

```ts
if (FOOD_PARSER_PROVIDER === "hermes" || FOOD_PARSER_PROVIDER === "codex") {
  return parseFoodTextWithHermes({
    text,
    model: model ?? DEFAULT_HERMES_MODEL,
  });
}
```

Hermes call:

```ts
const { stdout, stderr } = await execFileAsync(
  hermesCommand,
  [
    "chat",
    "--quiet",
    "--provider",
    hermesProvider,
    "--model",
    model,
    "--query",
    prompt,
  ],
  {
    timeout: 120_000,
    maxBuffer: 1024 * 1024,
    env: { ...process.env, NO_COLOR: "1" },
  },
);
```

Then extract JSON from stdout and validate with the existing schema:

```ts
return parseAndValidateFoodJson(extractJsonObject(stdout), `${hermesProvider}/${model}`);
```

## `.env.example` shape

```env
DATABASE_URL="postgresql://fitness:***@localhost:5432/fitness?schema=public"

# Default: run food parsing through local Hermes/Codex OAuth, no app API key needed.
# Requires Hermes CLI to be installed and authenticated on the server running Next.js.
FOOD_PARSER_PROVIDER="hermes"
HERMES_FOOD_COMMAND="hermes"
HERMES_FOOD_PROVIDER="openai-codex"
HERMES_FOOD_MODEL="gpt-5.4"

# Optional fallback if direct API mode is explicitly chosen later:
# FOOD_PARSER_PROVIDER="openai"
# OPENAI_API_KEY=""
# OPENAI_FOOD_MODEL="gpt-4o-mini"
```

## Verification used

```bash
npm run lint
npm run build
```

Also inspect `git diff` before committing. In this session, `npm install` changed `package-lock.json` metadata without a dependency change, so the lockfile was reverted before commit.

## Commit style used

```text
feat: support Hermes Codex food parser
```

## Caveat

This pattern is best for personal/self-hosted/server-side apps where Hermes is installed and authenticated on the deployment host. It is not a browser-side integration and should not expose CLI/model credentials to users.
