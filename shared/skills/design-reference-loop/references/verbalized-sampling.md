# Bounded creative exploration

Verbalized Sampling (VS) requests multiple responses and model-verbalized probabilities to encourage diversity. These numbers are not measured likelihoods, calibrated quality scores, confidence in correctness, or probabilities of product success. Do not use them to authorize actions or automatically choose a design.

Apply only when the visual direction is genuinely open. Skip for bugfixes, pixel-parity tasks and implementation of an already approved design. Use the active, authorized generator; no new provider subscription or fallback is implied. One initial candidate batch is the default; a further batch requires a concrete issue in the first set, not an endless self-critique loop.

## Copy-ready generation prompt

```text
For the following UI brief, propose 3 to 5 structurally different design directions.
Return each concept with a stable id, short summary, named macrostructure,
typography/spacing/palette roles, mobile behavior, primary action, constraints,
and one clear trade-off. Explore genuinely different compositions, not color swaps.
Include a self-estimated typicality probability only if it helps exploration;
label it as a model estimate, never a quality or correctness probability.
Do not write code, install dependencies, copy protected assets, or select a winner.
Respect the existing approved elements and budget. Explain conflicts explicitly.
Brief: <reviewed project brief>
```

Review the concepts against hard constraints. Host/human review, not the generator's own pass assertions, supplies any check attestations. Missing information stays unmeasured. Let the user compare a short list with clear trade-offs and choose before implementation.

The offline example is deliberately synthetic. It proves only data handling and filtering, not model creativity. Quality evaluation needs a real authorized design task with fixed grading and honest before/after evidence; reuse the stack's existing workflow-eval discipline rather than adding a benchmark service.

Primary source: https://github.com/CHATS-lab/verbalized-sampling and https://arxiv.org/abs/2510.01171 . This pack does not install or vendor that implementation.
