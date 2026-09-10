# Week 1 self-study and functions tutoring notes

Session-derived conventions for `rei-vault/topics/ai-engineering`.

## Why this exists

The user noticed normal guided lessons were taking only ~20 minutes and wanted a way to study 40–60 minutes without constantly calling Hermes, partly for token/cost control. The correct response is not to build a full quiz website immediately; add a lightweight self-study layer in the vault first.

## Self-study layer pattern

When lessons feel too short, add or maintain these markdown materials under:

```text
topics/ai-engineering/self-study/
```

Recommended files:

- `week-1-self-study.md` — session order: read → predict → write → run → compare → log.
- `week-1-python-cheatsheet.md` — compact theory for the current week.
- `week-1-drills.md` — extra exercises for independent practice.
- `week-1-answer-key.md` — answers for checking after attempting, not for copy-paste.

Use this before proposing a site/app. A quiz website can become a later learning project after functions/lists/files/JSON, not an early distraction.

## Token-saving lesson mode

Default flow when the user wants fewer Hermes calls:

1. User opens the daily note + current `.py` practice file.
2. User uses self-study cheatsheet and drills independently.
3. User only calls Hermes for confusing errors, output mismatch, concept checks, or day completion.
4. Hermes verifies by pulling the pushed repo, running the current day script, and updating the daily/progress files.

## Function-day misconception to handle

Common Day 4 issue: confusing `return` and `print`.

Teach the compact formula:

```text
return = отдаёт результат из функции наружу в код
print = показывает значение в консоли
```

If the user says “return возвращает ответ в функцию,” correct gently:

```text
Не в функцию, а из функции наружу.
```

Example:

```python
def add(a, b):
    return a + b

result = add(2, 3)  # result now stores 5
print(result)       # console shows 5
```

## Day completion verification pattern

When the user says they pushed a day to GitHub:

1. Fetch/fast-forward the audit clone.
2. Read the current day file and README/daily note.
3. Run the day script with Python.
4. Give feedback on the actual output.
5. Patch only small clarifications if needed.
6. Mark the daily note completed, run `sync_progress.py`, commit, pull --rebase, push.

Avoid declaring a day completed purely from the user's description if repo verification is available.
