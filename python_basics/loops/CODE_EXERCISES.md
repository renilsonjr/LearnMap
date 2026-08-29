# Loops — Code Exercises

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Write a `for` loop that prints numbers 1 through 10.
2. Write a `while` loop that counts down from 5 to 1 and then prints `"Liftoff!"`.
3. Write a loop over 1-20 that stops with `break` as soon as it reaches a multiple of 7.

## Medium
4. Write a loop over 1-20 that skips multiples of 3 with `continue` and prints the rest.
5. Write a `for` loop with an `else` clause that searches for a target value in a list and prints `"not found"` only if the loop completes without a `break`.
6. Write a script using `enumerate()` to print each item in a list alongside its index, formatted as `"0: apple"`.
7. Write a script using `zip()` to pair names and scores from two lists and print `"name: score"` for each pair.

## Hard
8. Write a custom iterable class `Countdown` implementing `__iter__`/`__next__` that counts down from a given number, and use it in a `for` loop.
9. Write a function `remove_evens(nums)` that safely removes all even numbers from a list while iterating, avoiding the classic mutate-while-iterating bug (explain the bug in a comment).
10. Write three versions of "square all numbers 1-100000 and sum them": a `for` loop, a list comprehension, and a generator expression; time or compare them with `sys.getsizeof` and comment on the results.
