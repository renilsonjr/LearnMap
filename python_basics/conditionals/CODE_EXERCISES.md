# Conditionals — Code Exercises

## Persona Prompt Block
**Role:** Technical Recruiter reviewing your take-home exercise.
**Rules:**
- Reads your code as if reviewing it before a call — clarity and correct naming count.
- Runs it and checks the printed output matches what was asked for.
- Calls out code that "happens to work" but wouldn't survive a slightly different input.
- Rewards concise, working code over long code that almost works.

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Write a function `classify_number(n)` that prints `"positive"`, `"negative"`, or `"zero"`.
2. Write a script that checks if a number is between 1 and 100 using `if/elif/else`.
3. Write a function `is_falsy(value)` that returns `True` for `0`, `""`, `None`, `[]`, and `False` for anything else, without using `==`.

## Medium
4. Write a function `max_of_three(a, b, c)` using a ternary/conditional expression.
5. Write a function `get_display_name(name)` that returns `"Anonymous"` if `name` is `None` or empty, otherwise returns `name`.
6. Write a script that uses the walrus operator to read a value, check it inside an `if`, and reuse the same value inside the block without recomputing it.
7. Write a function `check_access(is_admin, is_owner, is_banned)` that correctly combines `and`/`or` (with parentheses) to determine access.

## Hard
8. Rewrite a deeply nested `if/else` password validator (checks length, digit, uppercase) using early returns/guard clauses instead.
9. Write a function `describe_shape(shape)` using Python 3.10+ `match`/`case` to handle `"circle"`, `"square"`, `"triangle"`, and an unknown default.
10. Write `in_range_chain(x)` using a chained comparison (`0 < x < 10`) and a second version using explicit `and`; show they're equivalent and explain in a comment why chaining can't always be split this simply.
