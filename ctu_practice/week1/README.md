# Week 1 — Fundamentals — Theory Questions

Original questions about the concepts practiced in [the Week 1 code exercises](CODE_EXERCISES.md). Explain your reasoning in your own words; no code submission is required for these questions.

## Persona Prompt Block
**Role:** Introductory Python instructor reviewing your explanations.
**Rules:**
- Explain what Python does and why, using a small example when it helps.
- Distinguish the type of a value from how that value looks when printed.
- For debugging questions, identify the cause of the problem before suggesting a correction.

## Questions

### Easy
1. What is the difference between `print()` and `input()`? What type of value does `input()` give back?
2. How are the integer `250` and the string `"250"` different, even though they contain the same digits?
3. In `daily_rate * days * weeks`, what role does each variable play, and how does Python decide the result?

### Medium
4. A user types `12.5` at an `input()` prompt. Why can you not immediately add the result to the float `3.0`, and what conversion would make that calculation possible?
5. Compare `int("12")`, `float("12")`, and `float("12.5")`. What kind of value does each conversion produce, and what happens if the text cannot be interpreted as a number?
6. What does `:.2f` mean inside an f-string? Explain the difference between formatting a number for display and changing the number stored in a variable.
7. What makes a mismatched quote a syntax error, while using the wrong discount multiplier is a logic error? When would you notice each one?

### Hard
8. In the BMI expression `weight_kg / height_m ** 2`, explain how operator precedence affects the calculation. Why would `(weight_kg / height_m) ** 2` represent a different calculation?
9. A program reads three daily hours with `input()` and computes weekly pay. Walk through the values' types from input to final pay, and explain two different mistakes that could make the result wrong or crash the program.
10. A trip-time calculation produces a very small number of days. Explain why printing the same float to two decimal places and four decimal places can give a different impression of the result. How would you decide which display precision is useful?

---
Answers are withheld. Save your explanations in your own subfolder and open a pull request when you want a teammate to review them, following [the repository instructions](../../instructions.md).
