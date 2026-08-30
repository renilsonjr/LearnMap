# Basic Syntax — Code Exercises

## Persona Prompt Block
**Role:** PySyntax Bot — an automated grading platform (Grill.me-style) for Python fundamentals.
**Rules:**
- Runs your code and checks it executes without errors.
- Checks that the output matches the behavior described in the exercise, not just "looks about right."
- Flags any line that would violate basic PEP 8 (naming, spacing, indentation).
- Hard-tier submissions are also judged on whether they actually demonstrate the underlying concept, not just produce the right output by luck.

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise (`01_easy.py`, `02_easy.py`, ...), then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Write a script that prints `"Hello, World!"` to the console.
2. Write a script with a single-line comment above a `print()` call explaining what it does, then run it to confirm the comment is ignored at runtime.
3. Assign three variables in three separate lines, then print all three in one `print()` call separated by commas.

## Medium
4. Write a script that would raise an `IndentationError` if run as-is (leave the broken version in a comment) and then include the corrected, working version below it.
5. Write a function `greet(name)` with a multi-line docstring and a one-line body, keeping every line under 79 characters (PEP 8).
6. Write a script that sums 10 hard-coded numbers using an expression wrapped across three lines via implicit continuation inside parentheses.
7. Write one line with two statements separated by `;`, then rewrite it as two separate lines; add a comment explaining which style is preferred and why.

## Hard
8. Write a script whose value spans multiple lines using both an explicit `\` line continuation and an implicit continuation inside a list literal in the same file; print the final result.
9. Write a function that would raise a `SyntaxError` if written incorrectly (show the broken snippet as a comment/string, not as executable code) alongside the corrected, working version.
10. Write two versions of the same small function — one following PEP 8 exactly, one violating at least three style rules (naming, spacing, line length) — with comments marking each violation in the second version.
