# Operators — Code Exercises

## Persona Prompt Block
**Role:** Elite Academic Professor grading a lab assignment.
**Rules:**
- Requires code that actually runs and produces correct output — no partial credit for pseudocode.
- Deducts points for solutions that don't use the concept being tested (e.g. hardcoding an answer instead of computing it).
- Expects hard-tier exercises to include the comparison/explanation asked for, not just the code.
- Rewards code that generalizes beyond the one example shown.

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Write a script that takes two numbers and prints the results of `+`, `-`, `*`, `/`, `//`, `%`, and `**` applied to them.
2. Write a function `is_even(n)` using the modulo operator.
3. Write a script that compares two numbers using all six comparison operators and prints each result.

## Medium
4. Write a function `average(a, b, c)` that correctly uses `/` (not `//`) to compute a float average.
5. Write a script that evaluates `2 + 3 * 4 ** 2` step by step with intermediate variables to show precedence, then confirms the result matches the direct expression.
6. Write a function `apply_discount(price, percent)` that uses an augmented assignment operator to reduce a price by `percent`%.
7. Write a function `toggle_bit(n, position)` that uses bitwise operators (`^`, `<<`) to flip a single bit of an integer.

## Hard
8. Write a function `safe_divide(a, b, default=0)` that avoids a `ZeroDivisionError` using a conditional expression or short-circuit `or`.
9. Write a class `Vector` with `__add__` overloaded so `Vector(1, 2) + Vector(3, 4)` returns `Vector(4, 6)`; print the result.
10. Write a script demonstrating the difference between `a += [3]` and `a = a + [3]` on a list also referenced by another variable `b`, printing `b` after each approach.
