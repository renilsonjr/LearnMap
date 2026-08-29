# Sets — Code Exercises

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Create a set from a list with duplicate values and print it to show duplicates are removed.
2. Write a function `add_unique(s, value)` that adds a value to a set and returns the set.
3. Write a script that detects whether a list has duplicates by comparing its length to the length of `set(list)`.

## Medium
4. Write a function `common_elements(a, b)` that returns the intersection of two sets.
5. Write a function `safe_remove(s, value)` using `discard()` so removing a missing value doesn't raise an error; contrast with `remove()` in a comment.
6. Write a function `unique_words(text)` that returns the set of unique lowercase words in a sentence.
7. Create a `frozenset` from a list and demonstrate it can be used as a dictionary key while a regular set cannot.

## Hard
8. Write a script that attempts to put a list inside a set, catches/prints the resulting `TypeError`, then shows the fix using a tuple instead.
9. Write a benchmark comparing `x in list_of_1000` vs `x in set_of_1000` using `time.perf_counter()` over many lookups, printing both timings.
10. Write a function `only_in_a(a, b)` that returns items in list `a` but not in list `b` using set difference, and compare its logic to a nested-loop version in a comment.
