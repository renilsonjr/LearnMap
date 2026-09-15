# Week 1 — Fundamentals — Code Exercises

Original exercises inspired by Week 1 topics (print/input, type conversion, expressions, float formatting, debugging) — not copies of any CTU/zyBooks assignment. Write real, runnable Python for each item; put solutions in your own subfolder, no answer key included.

## Persona Prompt Block
**Role:** CS101 Auto-Grader — an automated system similar to the one your coursework already uses.
**Rules:**
- Runs your program with sample inputs and checks exact output, including decimal places, punctuation, and spacing.
- Any uncaught exception (crash) is an automatic fail for that test case.
- Small formatting slips (e.g. forgetting `:.2f`) cost partial credit even when the logic is right.
- Hard-tier exercises are graded on whether the formula/structure is actually correct, not just "produces a number."

## Easy
1. Write a script with fixed variables `daily_rate = 35`, `days = 6`, `weeks = 2` that computes and prints the total pay for a pet-sitter, using one `print()` call combining a label and the result.
2. Write a script that asks the user for their name and favorite color with two separate `input()` calls, then prints both on the same output line, separated by a comma (use `end=' '` at least once).
3. Convert the hard-coded string `"250"` into an integer, add `50` to it, and print both the original string and the new integer, each with its own label.

## Medium
4. Ask the user for a temperature in Celsius, convert it to a `float`, and print the equivalent Fahrenheit temperature (`F = C * 9/5 + 32`) formatted to exactly 2 decimal places.
5. Write a script with an intentional syntax error inside a comment (mismatched quotes in a `print()` call), then the corrected, working version below it — same idea as the `basic_syntax` indentation-error exercise, but for a quote mismatch instead.
6. Ask for three separate purchase amounts (as input, converted to `float`) and print their average formatted to 2 decimal places, labeled `"Average purchase: $X.XX"`.
7. Write a script with a logic bug: it's meant to apply a 10% discount but multiplies the price by `10` instead of `0.10`. Leave the buggy version commented above the fixed, working version.

## Hard
8. Write a program that reads `weight_kg` and `height_m` (both floats, from input), computes BMI (`weight_kg / height_m ** 2`), and prints the result formatted to 2 decimal places with a labeled message.
9. Write a program that reads three separate inputs for hours worked on three different days, sums them using an expression wrapped across multiple lines inside parentheses (implicit continuation, like the `basic_syntax` line-continuation exercise), multiplies by an hourly wage of `18`, and prints the weekly pay.
10. Write a program that reads `distance_km` (float, input) and uses `speed_kmh = 27000` to compute how many days a trip would take; print the result once formatted to 4 decimal places, and again formatted to 2 decimal places, each with its own label.
