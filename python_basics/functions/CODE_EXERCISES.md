# Functions, Builtin Functions — Code Exercises

## Persona Prompt Block
**Role:** Elite Academic Professor grading a lab assignment.
**Rules:**
- Requires code that actually runs and produces correct output — no partial credit for pseudocode.
- Deducts points for solutions that don't use the concept being tested (e.g. hardcoding an answer instead of computing it).
- Expects hard-tier exercises to include the comparison/explanation asked for, not just the code.
- Rewards code that generalizes beyond the one example shown.

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Write a function `square(n)` that returns `n` squared.
2. Write a function `greet()` with no parameters that returns `"Hello!"`.
3. Write a script that calls `len()`, `max()`, and `sorted()` on a list and prints each result.

## Medium
4. Write a function `introduce(name, age=None)` with a default parameter, callable with just `name` or with both arguments.
5. Write a function `add_item(item, lst=None)` that avoids the mutable-default-argument bug by defaulting to `None` and creating a new list inside the function.
6. Write a function `total(*args, **kwargs)` that sums all positional numeric args and prints any keyword arguments separately.
7. Write a one-line lambda that squares a number, and an equivalent `def` function; use both with `map()` on a list.

## Hard
8. Write a function `make_multiplier(factor)` that returns a nested function (closure) multiplying its input by `factor`; create two multipliers and use both.
9. Write a script using `map()` and `filter()` together (plus a helper function) to square only the even numbers in a list.
10. Write a nested function that reads an enclosing variable, then a second version that uses `nonlocal` to modify it, printing the difference in behavior.
