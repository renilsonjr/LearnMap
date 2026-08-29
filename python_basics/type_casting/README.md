# Type Casting — Practice Questions

## Persona Prompt Block
**Role:** Technical Recruiter running a phone-screen on Python fundamentals.
**Rules:**
- Looking for clear, confident communication as much as correctness — explain your answer like you're on a call.
- Follow-up questions probe "why," not just "what."
- Buzzwords without substance are called out.
- A wrong answer with good reasoning scores better than a right answer with no explanation.

## Questions

### Easy
1. How do you convert a string `"42"` into an integer?
2. What function converts a number into a string?
3. What happens if you try to convert `"abc"` into an integer with `int()`?

### Medium
4. What is the difference between implicit and explicit type conversion in Python? Give an example of each.
5. How do you convert a list into a set, and what happens to duplicate values?
6. What does `float("3.14")` return, and how does it differ from `int("3.14")`, which fails?
7. How would you convert a list of strings representing numbers into a list of integers in one line?

### Hard
8. Explain what happens when Python implicitly converts a `bool` to an `int` in arithmetic (e.g. `True + True`), and why this works.
9. Describe a real bug scenario caused by silently truncating a `float` to an `int` via `int()` instead of rounding, and how you'd fix it.
10. Explain how `bool()` casting works for different types (empty vs. non-empty strings/lists/dicts, zero vs. non-zero numbers) and why this matters for writing correct `if` conditions.

---
Answers are withheld here. Solve these in your own subfolder and open a PR, per [../../instrucoes.MD](../../instrucoes.MD).
