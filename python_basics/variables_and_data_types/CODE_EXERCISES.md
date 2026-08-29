# Variables and Data Types — Code Exercises

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Create variables of type `int`, `float`, `str`, `bool`, and `None`, then print each value together with its `type()`.
2. Write a script that swaps the values of two variables without using a third variable.
3. Write a function `describe(value)` that returns a string like `"3 is an int"` for any input, using `type(value).__name__`.

## Medium
4. Write a script that reassigns the same variable to an `int`, then a `str`, then a `list`, printing the type after each reassignment.
5. Write a function `is_mutable(value)` that returns `True`/`False` depending on whether the given value's type is mutable.
6. Create a list and a tuple with identical contents, attempt to modify one element of each, and catch/print the error raised by the tuple.
7. Write a function `is_valid_variable_name(name)` that checks a string against Python's naming rules (starts with letter/underscore, no spaces, not a reserved keyword).

## Hard
8. Write a script that creates a list `b`, sets `a = b`, mutates `a`, and prints `b` to demonstrate both names reference the same object.
9. Write a script comparing `is` vs `==` for two lists with identical contents and for two small integers, printing all four results.
10. Write a script demonstrating integer interning by comparing `a is b` for `a, b = 5, 5` versus `a, b = 1000, 1000`, printing both booleans and the `id()` of each variable.
