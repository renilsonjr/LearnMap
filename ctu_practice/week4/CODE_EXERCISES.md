# Week 4 — Functions — Code Exercises

Original exercises inspired by Week 4 topics (defining functions, parameters, `return`, one function calling another, missing-return bugs, returning multiple values, variable scope, and the `if __name__ == "__main__":` guard) — not copies of any CTU/zyBooks assignment. Write real, runnable Python for each item; put solutions in your own subfolder, no answer key included.

## Persona Prompt Block
**Role:** CS101 Auto-Grader — an automated system similar to the one your coursework already uses.
**Rules:**
- Runs your program with sample inputs and checks exact output, including decimal places, punctuation, and spacing.
- Any uncaught exception (crash), or a function that returns `None` when a value was expected, is an automatic fail for that test case.
- Function and variable names must match exactly, including capitalization — a case mismatch between a `def` and a call is treated as a bug, not a typo.
- Hard-tier exercises are graded on whether the function structure (parameters, `return`, scope) is actually correct, not just whether one sample input happens to work.

## Easy
1. Write a function `square(n)` that returns `n` squared. Call it with `4` and `9` and print both results.
2. Write a function `greet(name)` that takes one parameter and returns a greeting string built from it. Call it with two different names and print both results.
3. Write a function `get_stars()` that takes no parameters and returns the string `'***'`. Call it twice, each time inside its own `print()`, so six stars print in total across two lines.

## Medium
4. Write a function `rectangle_area(width, height)` with two parameters that returns the area. Call it with two different width/height pairs and print both results.
5. Write two functions: `circle_area(radius)` that returns the area of a circle, and `cylinder_volume(radius, height)` that calls `circle_area()` internally and returns the volume. Print the volume for one radius/height pair.
6. Write a function `minutes_to_hours(minutes)` with an intentional bug where it forgets the `return` statement (leave the buggy version commented, showing what printing its result actually gives), then the corrected, working version below it.
7. Write a function `get_order_total(price, tax_rate)` that returns **two** values as a tuple: the tax amount and the total price. Call it, unpack both values into separate variables, and print them with labels.

## Hard
8. Write a script demonstrating variable scope: a global variable `visitor_count = 0`, and a function `log_visit()` that uses the `global` keyword to increment it by 1 each call. Call the function three times, then print the final count.
9. Write a script with a function-name bug: define a function with one capitalization (for example `calc_Bonus`) but call it elsewhere with different capitalization, and leave that broken version as a comment showing the error it produces. Below it, write the corrected, working version where the definition and every call match exactly.
10. Write a program using the `if __name__ == "__main__":` guard: define a function `km_to_miles(km)` that returns the equivalent distance in miles (1 km = 0.621371 miles), formatted to 2 decimal places inside an f-string when printed. Put the input-reading and printing logic inside the `if __name__ == "__main__":` block, not at the top level of the file.
