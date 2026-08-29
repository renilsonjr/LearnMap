# Type Casting — Code Exercises

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Write a function `to_int(s)` that converts a numeric string to an `int` and prints the result and its type.
2. Write a function `number_to_string(n)` that converts a number to a string and concatenates it with `" items"`.
3. Write a script that attempts `int("abc")`, catches the `ValueError`, and prints a friendly error message.

## Medium
4. Write a script demonstrating implicit conversion (`1 + 2.0`) and explicit conversion (`int(2.9)`), printing both results and their types.
5. Write a function `unique_count(lst)` that converts a list to a set to count unique elements, printing the count.
6. Write a script comparing `float("3.14")` (succeeds) with `int("3.14")` (fails), catching the error for the second case.
7. Write a function `strings_to_ints(str_list)` that converts a list of numeric strings into a list of integers using a list comprehension.

## Hard
8. Write a script showing `True + True` and `False + 5`, printing the results and explaining the `bool`-as-`int` behavior in a comment.
9. Write a function `to_cents(price)` that correctly rounds a float price to the nearest cent using `round()` instead of truncating with `int()`; show the bug truncation would cause with `19.999`.
10. Write a function `truthy_report(values)` that takes a list of mixed values (`0`, `1`, `""`, `"a"`, `[]`, `[1]`, `None`) and prints each value alongside its `bool()` cast.
