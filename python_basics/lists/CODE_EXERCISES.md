# Lists — Code Exercises

## Persona Prompt Block
**Role:** Grill.me-style automated testing platform.
**Rules:**
- Auto-runs each submission and checks output against expected results.
- Any uncaught exception on valid input is an automatic fail for that exercise.
- Style and edge-case handling affect the score even when the "happy path" output is correct.
- Hard-tier exercises are graded on whether the required comparison/explanation is actually present in comments or print output, not just implied.

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Create an empty list, append three items to it, and print the final list.
2. Write a function `third_item(lst)` that returns the third element of a list.
3. Write a function `pop_last(lst)` that removes and returns the last element of a list.

## Medium
4. Write a function `reverse_list(lst)` using slicing (no `.reverse()` or `reversed()`).
5. Write a function `sort_copy(lst)` that returns a new sorted list without modifying the original, and contrast it with a version that uses `.sort()`.
6. Rewrite `[x*2 for x in range(5) if x % 2 == 0]` as an equivalent `for` loop that builds the same list.
7. Write a function `dedupe_preserve_order(lst)` that removes duplicates while preserving the original order.

## Hard
8. Write a function `deep_vs_shallow(matrix)` that shallow-copies and deep-copies a list of lists, mutates an inner list in the shallow copy, and prints both copies to show the difference.
9. Use `collections.deque` to repeatedly insert at the front of a large sequence, and compare its behavior/cost in a comment to `list.insert(0, x)`.
10. Write `counter(lst=[])` that demonstrates the mutable-default-argument bug (state leaking across calls), then fix it using `None` as the default.
