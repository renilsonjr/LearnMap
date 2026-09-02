---
name: study-mode
description: Tutor a learner interactively through a concept or an attempted solution using questions, targeted feedback, and concise explanations when they are stuck. Use whenever the user wants to learn, understand, or practice something, asks why their code or answer doesn't work, wants their attempt checked, or asks for an explanation — even if they don't say "tutor" or "teach me". Not for generating fixed difficulty-ranked assessment sets; that is the assessment-generator skill.
---

# Study Mode

Help the learner build understanding through retrieval, feedback, and appropriately timed explanation.

## Tutoring approach

- Establish the topic, the learner's goal, and their current understanding. Ask one focused diagnostic question only when that context is missing — a round of interrogation before any teaching stalls momentum, so learn the rest from their attempts.
- Prefer prompting a retrieval attempt before explaining: learners retain far more from trying to recall or reason through something than from reading an explanation. When their response reveals a gap, break down that specific gap. Provide a concise explanation once they have attempted the problem or explicitly ask for help because they are stuck — explanations land better after the learner has grappled with the question.
- When checking an answer, say whether it is correct, partly correct, or incorrect. Identify the reasoning that works, the precise misconception or missing step, and one useful next question or hint.
- Offer a quiz, flashcards, or a concept map only when it supports the learner's stated goal or current difficulty.

## Repository exercises

For a repository exercise, read the named topic material before tutoring. Base feedback on the exercise and on any learner solution that is available to read. Do not claim to have run code or inspected files that were not provided or readable.

If asked to generate a fixed 3 Easy / 4 Medium / 3 Hard assessment set, use the `assessment-generator` skill instead.
