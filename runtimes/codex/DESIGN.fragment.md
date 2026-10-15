# Design skills routing — manual fragment

Merge into the intended Codex instructions only after selecting and reviewing the available skills. Preserve existing project policy and explicit-only invocation rules. This fragment neither installs skills nor changes runtime permissions.

For visual design, choose and read a small relevant installed set without requiring the user to name it:

- Landing pages, portfolios and expressive redesigns: `design-taste-frontend`; use `gpt-taste` or `design-taste-frontend-v1` when their scope fits better. Add `brandkit`, minimalist, brutalist or high-end style guidance only when the brief calls for it.
- Product interfaces and interaction details: `emil-design-eng` and `impeccable-design`. Add the relevant animation or native-platform skill when needed.
- Documents, reports and presentations: follow the artifact-specific skill first; apply Impeccable principles for hierarchy, typography, contrast, spacing and readability where relevant.
- Refinement: use the relevant Impeccable audit or polish playbook while preserving established branding and behavior.
- When direction is unresolved, use `design-reference-loop` for bounded exploration and user choice. Skip exploration for exact implementation, approved designs and bugfixes.

`prototype`, `pick-ui-library` and `review-animations` run only when explicitly invoked. Do not implicitly load them through this routing policy. Their `agents/openai.yaml` metadata is preserved. Image-generation and other specialized capabilities require actual supported host tools; do not invent tool names or treat a missing capability as installed.

The user's brief, existing brand, project architecture and applicable instructions take priority over general style preferences. Dependency installation examples require the user's authorization and compatible versions. No skill grants authority to install dependencies, publish, send data, change credentials or control the computer. Impeccable is the static playbook adaptation; do not add its excluded engine, launchers, hooks or live server. Verify changes through supported tools and report only observed results.
