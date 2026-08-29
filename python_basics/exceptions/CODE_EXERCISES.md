# Exceptions — Code Exercises

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Write a script that divides by zero inside a `try/except` and prints a friendly error message instead of crashing.
2. Write a function `safe_int(s)` that returns `None` instead of raising when `s` isn't a valid integer string.
3. Write a script using `try/except/finally` that always prints `"Done"` regardless of whether an error occurred.

## Medium
4. Write a function `parse_age(value)` that catches `ValueError` specifically (not a bare `except`) when converting input to an int.
5. Define a custom exception `InsufficientFundsError` and raise it from `withdraw(balance, amount)` when `amount > balance`.
6. Write a function `divide(a, b)` using `try/except/else` where the `else` block only runs when no exception occurred.
7. Write a function `parse_value(s)` that catches both `ValueError` and `TypeError` in a single `except` clause.

## Hard
8. Write a function that catches a low-level exception and re-raises a higher-level custom exception using `raise ... from ...`, preserving the original context.
9. Write a script explaining (with a comment and a safe simulation, e.g. catching `SystemExit`) why a bare `except:` is dangerous compared to `except Exception:`.
10. Write `get_config_value(d, key)` twice: once EAFP style (`try/except KeyError`) and once LBYL style (`if key in d`), with comments comparing the two.
