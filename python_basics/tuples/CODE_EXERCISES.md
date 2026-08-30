# Tuples — Code Exercises

## Persona Prompt Block
**Role:** Technical Recruiter reviewing your take-home exercise.
**Rules:**
- Reads your code as if reviewing it before a call — clarity and correct naming count.
- Runs it and checks the printed output matches what was asked for.
- Calls out code that "happens to work" but wouldn't survive a slightly different input.
- Rewards concise, working code over long code that almost works.

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Create a tuple with three elements (a name, age, and city) and print each element by index.
2. Write a script that attempts to modify an element of a tuple and catches/prints the resulting `TypeError`.
3. Create a single-element tuple correctly (with the trailing comma) and print its type to confirm.

## Medium
4. Write a script that swaps two variables using tuple unpacking in a single line.
5. Write a function `min_max(numbers)` that returns a tuple `(min, max)` instead of two separate return values.
6. Write a function `sum_all(*args)` that accepts any number of arguments as a tuple and returns their sum.
7. Define a `namedtuple` called `Point` with fields `x` and `y`, create two points, and print their sum as a new tuple.

## Hard
8. Write a script that stores tuples as dictionary keys (e.g. coordinates `(x, y)`) and explain in a comment why a list couldn't be used the same way.
9. Write a script with a tuple containing a list, mutate the inner list, and print the tuple before/after to show it "changed" despite being immutable.
10. Write a benchmark script comparing the memory footprint (`sys.getsizeof`) of a tuple vs. a list holding the same 5 integers.
