# EU Relocation / Career / Financial Layer for AI Engineering Learning

Session-derived pattern for handling long-term relocation, admissions, and financial strategy inside `rei-vault/topics/ai-engineering`.

## When this applies

Use when the user brings in notes about:

- EU / global bachelor routes for CS, AI Engineering, Data Science, or Software Engineering;
- relocation strategy;
- visas, residence permits, proof of funds, blocked accounts, GICs, sponsor docs;
- admissions after Russian СПО / college;
- tuition, living costs, scholarships, stipends, and first-year cash requirements;
- country rankings, shortlist decisions, and ROI;
- portfolio projects for university/career positioning;
- career narrative linking AI engineering study to education/relocation.

## Classification

These notes are **career/admission/financial strategy**, not daily study material.

They answer:

```text
Why this learning path matters, where it can lead, and what constraints shape the route.
```

They do **not** answer:

```text
What Python exercise should be done today?
```

## Recommended structure

Keep the layer under:

```text
topics/ai-engineering/career/
├── eu-ai-engineering-relocation-strategy.md
├── eu-relocation-action-plan.md
├── eu-extended-country-map.md
├── global-non-eu-study-routes.md
├── financial-reality-map-2026-2027.md
└── financial-action-checklist.md
```

Meaning:

- `eu-ai-engineering-relocation-strategy.md` — large EU education/career/admission strategy.
- `eu-relocation-action-plan.md` — short operational relocation checklist.
- `eu-extended-country-map.md` — secondary EU country filter map.
- `global-non-eu-study-routes.md` — Canada/USA/UK/Australia/NZ global backup map.
- `financial-reality-map-2026-2027.md` — large financial map with tuition, living costs, visa proof, scholarships, work rights, post-study rights, hidden costs, first-year money, monthly survival budgets, rankings, and questions to email universities.
- `financial-action-checklist.md` — short financial operating checklist with budget buckets, emergency reserve, bank/sponsor docs, deposit/refund checks, visa proof tasks, hidden costs, and 2026-2027 checkpoints.

## File handling pattern

1. Pull/sync the repo first and inspect the latest commit when the user says they added files.
2. Identify newly added relocation/career/financial notes from `git show --name-status HEAD` or the equivalent repo state.
3. Read the new notes before editing; check whether they are complete or truncated.
4. Rename messy uploaded files to clean kebab-case.
   - Bad: `relocation ai engeneering in eu.md`
   - Good: `eu-ai-engineering-relocation-strategy.md`
   - Bad: `financial_map_relocation_2026_2027.md`
   - Good: `financial-reality-map-2026-2027.md`
5. Put long strategic docs under `topics/ai-engineering/career/`.
6. Add a top note with:
   - `Status: ...`
   - `Last checked: YYYY-MM`
   - `Review again: YYYY-MM, YYYY-MM, ...`
   - `Role: ...`
   - warning that visa/finance/admission data needs official-source re-check.
7. Create a short action-plan/checklist note if the strategy is long.
8. Link long and short notes from `index.md` under `Career / relocation`.
9. Mention the layer in `roadmap-guidance.md` only as long-term context, not the operational daily plan.
10. Commit and push as a focused docs commit.

## Financial layer pattern

For finance/cost-of-living research, preserve two levels:

### 1. Large source map

Use a file like:

```text
financial-reality-map-2026-2027.md
```

It should hold detailed country-by-country planning data:

- tuition / semester fees;
- monthly and yearly living costs;
- visa/residence financial proof;
- blocked account / GIC / sponsor / bank statement rules;
- work rights during studies;
- post-study work route;
- scholarships/stipends/tuition waivers;
- hidden costs;
- bare minimum / realistic safe / comfortable first-year money;
- monthly survival/normal/safer budget;
- visa/admission/housing/job-market/immigration risk;
- ROI score and recommendation;
- rankings and final shortlist;
- questions to email admissions and scholarship offices.

Mark it as planning data, not visa/legal advice.

### 2. Short operational checklist

Use a file like:

```text
financial-action-checklist.md
```

It should be short enough for daily use and include:

- budget buckets: low-cost EU, premium EU, Anglosphere/global backup;
- realistic safe first-year estimates;
- emergency reserve after arrival;
- bank history checklist;
- sponsor docs checklist;
- tuition/deposit/refund checks;
- visa proof checklist;
- hidden costs checklist;
- financial priority shortlist;
- 2026-2027 checkpoints;
- anti-chaos reminder that learning/portfolio still matter.

## Current strategic interpretation

Default summary from the current research layer:

```text
Primary: Poland + Germany.
Non-EU serious backup: Canada.
EU backups: Austria + Italy + Finland + Hungary.
Expensive high-upside stretch: Netherlands + USA + UK.
Only with special conditions: Luxembourg, Australia, New Zealand.
```

Treat this as a planning snapshot, not permanent truth.

## Anti-chaos rule

Relocation/admission/financial notes can motivate learning, but they must not cause premature jumps into advanced projects or endless country research.

If a strategy says:

```text
LLM/RAG tutor, AI agent, full-stack AI app
```

translate it into prerequisite ladder:

```text
Python script → JSON tool → API client → small CLI app → simple LLM API app → larger portfolio project
```

If financial planning starts eating study time, return to:

```text
The cheapest route is useless if the user cannot pass CS/AI admissions or build a portfolio.
```

Nearest useful learning action remains:

```text
write Python by hand and finish small GitHub-readable projects
```

## Pitfalls

- Do not let relocation/finance planning replace the current lesson.
- Do not treat AI-generated visa/admission/finance numbers as permanently true; add review dates and official-source re-check reminders.
- Do not store huge raw dumps only; create a short checklist/action note next to large maps.
- Do not over-polish into a corporate strategy doc; keep notes usable in Obsidian.
- Do not create a second source of truth outside `rei-vault/topics/ai-engineering`.
- Do not choose countries purely by apparent visa simplicity; check tuition + housing + proof of funds + post-study route + job market.
