# Dictionaries — Code Exercises

## Persona Prompt Block
**Role:** Grill.me-style automated testing platform.
**Rules:**
- Auto-runs each submission and checks output against expected results.
- Any uncaught exception on valid input is an automatic fail for that exercise.
- Style and edge-case handling affect the score even when the "happy path" output is correct.
- Hard-tier exercises are graded on whether the required comparison/explanation is actually present in comments or print output, not just implied.

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Create a dictionary with three key-value pairs representing a person (name, age, city) and print each value.
2. Write a function `safe_get(d, key)` that returns the value for `key` or `"N/A"` if missing, using `.get()`.
3. Write a script that prints all the keys of a dictionary as a list.

## Medium
4. Write a function `get_or_default(d, key, default)` comparing `.get(key, default)` vs `d[key]` when the key is missing (catch the exception for the latter).
5. Write a script that iterates over a dictionary's `.items()` and prints `"key: value"` for each pair.
6. Write a dictionary comprehension that maps numbers 1-5 to their squares, then print it.
7. Write a script that merges two dictionaries using the `|` operator (Python 3.9+) and prints the result.

## Hard
8. Write a script that attempts to use a list as a dictionary key, catches/prints the resulting `TypeError`, then fixes it using a tuple.
9. Write a script that builds a dictionary by inserting keys in a specific order, then prints it to demonstrate that insertion order is preserved.
10. Write a simple hash table simulation (a list of buckets) that stores key-value pairs and demonstrates a collision, to illustrate how `dict` works internally.
