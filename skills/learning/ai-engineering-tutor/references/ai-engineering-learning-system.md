# AI Engineering Learning System — Session Reference

Use this reference when tutoring the user inside `rei-vault/topics/ai-engineering`.

## Current shape

The AI engineering learning system lives inside the existing Obsidian vault/repo, not a separate vault:

- `topics/ai-engineering/index.md` — entry point and quick links.
- `topics/ai-engineering/roadmap.md` — operational learning roadmap.
- `topics/ai-engineering/roadmap-guidance.md` — anti-chaos guidance and long-term filters.
- `topics/ai-engineering/week-1-start-guide.md` — immediate Week 1 Python-first route.
- `topics/ai-engineering/prompts/ai-engineering-tutor-skill.md` — vault-visible copy of tutor behaviour.
- `topics/ai-engineering/resources/ai-engineering-from-scratch.md` — long-term external curriculum spine.
- `topics/ai-engineering/career/` — career/relocation strategy layer.

## Teaching stance imported from external tutor skills

The session compared multiple tutor-oriented agent skills and chose to import only a compact core, not a heavy external platform.

Default loop:

```text
Recall → Explain → Example → Check → Evaluate → Practice → Log
```

Practical rules:

- Start continuing lessons with 1–3 tiny recall questions.
- Explain briefly; avoid long theory dumps.
- Show one concrete example.
- Ask the learner to predict output, explain in their own words, or change a small piece of code.
- Use the smallest useful hint before giving the answer.
- Do not behave like a strict Socratic bot all the time; direct explanation is allowed when the user is stuck.
- Use mastery gates lightly: do not advance if the user cannot explain/apply/fix a tiny example.
- If mistakes or questions repeat, suggest logging them in the vault rather than silently correcting forever.

## External curriculum role

`AI Engineering from Scratch` is treated as a long-term curriculum spine and map, not the daily plan.

Use it to:

- keep sequencing sane from foundations → ML → LLMs → agents → production;
- choose future topics;
- prevent random topic hopping.

Do not use it to:

- replace Week 1;
- dump 20 phases on the user;
- push agents/RAG/production before Python/files/JSON/API basics.

## Career / relocation layer

Career files are useful motivation and strategic direction, but must not override the learning sequence.

Current files:

- `career/eu-ai-engineering-relocation-strategy.md` — big EU education/career strategy.
- `career/eu-relocation-action-plan.md` — short operational checklist.
- `career/eu-extended-country-map.md` — secondary Europe shortlist and country filter.
- `career/global-non-eu-study-routes.md` — Canada/USA/UK/Australia/NZ backup map.

Working interpretation:

- Core: Poland + Germany.
- Global backup: Canada.
- EU secondary shortlist: Italy, Netherlands, Finland, Hungary, Luxembourg.
- Stretch / expensive backups: USA, UK, Australia, New Zealand, Denmark/Sweden if scholarship or strong budget.
- Mostly avoid as primary AI education route: Baltics for ordinary РФ bachelor route, Czechia as primary plan, private visa colleges, Georgia/Armenia/Moldova as education-to-EU-market route.

Always frame relocation strategy as `why this learning matters`, not as a reason to derail the current Python-first practice.

## Repo/Obsidian organization pattern

When the user drops large strategy files into the root of `topics/ai-engineering`, prefer to:

1. Read and classify the file.
2. Propose/perform a clean move into the right subfolder.
3. Rename to lowercase kebab-case without spaces or typos.
4. Add a short front-matter-like header: `Status`, `Last checked`, `Review again`, `Role`.
5. Add links from `index.md`.
6. Update a short action/checklist file only with the distilled operational conclusions.
7. Preserve the anti-chaos rule: the file informs strategy but does not replace Week 1 practice.
