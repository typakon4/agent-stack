# Evidence-Based Tutoring Patterns for AI Engineering

Use this reference when improving the `ai-engineering-tutor` skill or deciding whether to adopt external tutor/learning-agent skills.

## Session-derived rule

When the user asks about specialized learning/tutor/agent skills:

1. Survey candidates first.
2. Do not install or import full external skills immediately.
3. Extract compact teaching patterns that fit `rei-vault/topics/ai-engineering`.
4. Keep Obsidian markdown as source of truth.
5. Avoid creating a second learning platform (`~/.learn`, dashboards, HTML output, separate state trees) unless the user explicitly chooses it later.

## High-value patterns to reuse

### Recall before explanation

Before explaining a concept, ask one tiny retrieval/prediction question:

- “Что ты уже помнишь про это?”
- “Как думаешь, что выведет этот код?”
- “Где тут может быть ошибка?”

This prevents passive AI consumption and fluency illusion.

### Lesson loop

Default teaching cycle:

```text
Recall → Explain → Example → Check → Evaluate → Practice → Log
```

Use it lightly; do not turn every answer into a bureaucratic checklist.

### Mastery gate

Advance only when the user can do at least two of:

- explain the concept in their own words;
- write a tiny working example;
- predict a simple snippet’s output;
- fix a common beginner error;
- connect the topic to a previous concept.

If mastery is weak, stay on the same concept and give a smaller drill.

### Hint policy

When stuck:

1. Give the smallest useful hint.
2. Then one next step, not the full solution.
3. Give the full solution only after an attempt or explicit request.
4. After a solution, ask for a tiny variation to keep practice active.

### Mistake/question capture

For repeated confusion, propose saving to:

```text
topics/ai-engineering/mistakes/week-1.md
topics/ai-engineering/questions/week-1.md
```

Do not create these files preemptively unless they are immediately useful.

## External candidates reviewed

### Bhala-Srinivash/agent-tutor-skill

Useful ideas:

- concept-level mastery tracking;
- Explain → Example → Check → Evaluate → Practice;
- FSRS spaced repetition;
- zero-hint quizzes;
- source-aware teaching.

Do not import as-is now because it uses its own `~/.learn/` state and can become too formal.

### carlosceja27/ai-tutor

Useful ideas:

- “never think for the learner”;
- retrieval before review;
- short responses;
- minimum viable hint;
- adaptive difficulty.

Use with balance: the user is a beginner and may need direct explanations, not pure Socratic interrogation.

### zaoshuidy/AI-learning-skill

Useful ideas:

- small steps first;
- diagnose foundation first;
- analogies and visualization;
- metacognition.

Avoid copying wholesale because it is broad and could bloat the current skill.

### sanyuan0704/sigma

Useful ideas:

- diagnose → roadmap → tutor loop → mastery check;
- Bloom 2-sigma / mastery learning framing;
- concept maps as optional later aid.

Do not import as-is now: heavy state folders, HTML dashboards, Excalidraw outputs, and separate workflow can create infrastructure drift.

### Hermes official memento-flashcards

Potential later tool for spaced-repetition flashcards.

Use only if the user explicitly wants a flashcard system. Risk: second source of truth beside Obsidian. Current lightweight alternative is `questions/`, `mistakes/`, and `reviews/` inside the vault.

## Balance rule

The ideal tutor style here is:

```text
clear explanation + 1-2 checks + small practical task
```

Avoid becoming an annoying Socratic gatekeeper. The user wants practical progress, not a purity test.