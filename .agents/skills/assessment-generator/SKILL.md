---
name: assessment-generator
description: Create or update difficulty-ranked practice material for a learning topic — a theory quiz (README.md) and a hands-on coding exercise set (CODE_EXERCISES.md), each with 10 items in a 3 Easy / 4 Medium / 3 Hard split — and grade learner answers submitted against those sets. Use whenever the user asks for practice questions, a quiz, exercises, or test material for a topic, mentions difficulty-ranked or easy/medium/hard questions, or wants an answer to one of these sets checked — even if they don't say "assessment". Not for open-ended live tutoring or explaining concepts; that is the study-mode skill.
---

# Assessment Generator

Create practice material for one named learning topic.

## Determine the mode and target

- If the user asks to create or update files and names a topic folder, inspect that folder first. Preserve its language, filenames, and unrelated learner work.
- If the user does not give a target path, return the requested material in the response rather than modifying a repository file based on a guessed location.
- Use the target material to determine the implementation language. For a language-independent topic, let the learner choose an implementation language; otherwise, make coding exercises use the established language.
- If the topic folder has no established pattern, follow this repository's convention: a topic folder containing `README.md` (theory) and `CODE_EXERCISES.md` (hands-on), with learners solving in a personal subfolder and opening a PR. See `instrucoes.MD` for the full workflow.

## Deliverables

For a topic folder, produce the requested artifacts:

- `README.md` contains 10 theory questions: 3 Easy, 4 Medium, and 3 Hard.
- `CODE_EXERCISES.md` contains 10 hands-on coding exercises with the same 3/4/3 distribution.

Begin each artifact with a persona block suited to the topic, so the learner knows how their answers will be judged. Existing folders use this format — match it unless the folder has established something else:

```markdown
## Persona Prompt Block
**Role:** Technical Recruiter running a phone-screen on Python fundamentals.
**Rules:**
- Looking for clear, confident communication as much as correctness.
- Follow-up questions probe "why," not just "what."
- A wrong answer with good reasoning scores better than a right answer with no explanation.
```

Vary the persona across topics (recruiter, professor, automated grader, ...) so different folders exercise different answer styles.

Calibrate difficulty consistently across topics:

- **Easy**: direct use of a single core concept (e.g. "What does `break` do?" / "Write a loop that prints 1–10").
- **Medium**: combining concepts, or less-common features of the topic (e.g. the `else` clause on a loop, `enumerate()`/`zip()`).
- **Hard**: mechanisms under the hood, design tradeoffs, or items that demand an explanation or comparison alongside the answer.

The two sets should assess complementary skills, be answerable from the stated topic, and contain no solutions or answer key — withheld answers are what make the retrieval practice and PR review worthwhile. Match the existing files' structure: the theory `README.md` ends with a note that answers are withheld and that solutions go in a personal subfolder with a PR, while the exercises file carries that instruction as a lead-in line right after the persona block (see `python_basics/loops/` for both shapes).

When updating an existing generated file, change only the assessment content or the sections the user identifies. Do not overwrite learner solutions or unrelated documentation.

## Reviewing answers

When a learner submits an answer to one of these sets, assess it against the active persona block. State what is correct, what is missing or mistaken, and a useful next hint. Give a worked solution only when the learner explicitly requests one. For open-ended tutoring not tied to a fixed set, the `study-mode` skill is a better fit.

## Check before completion

- Each requested set has exactly 10 non-duplicative items in a 3 Easy / 4 Medium / 3 Hard split.
- The questions and exercises match the named topic and established language convention.
- The persona block and an answers-withheld notice are present.
- Any saved files are in the requested target folder with the expected names.
