# Week 2 — Conditionals — Code Exercises

Original exercises inspired by Week 2 topics (if/elif/else, boolean logic, nested ifs, indentation, dictionary lookups) — not copies of any CTU/zyBooks assignment. Write real, runnable Python for each item; put solutions in your own subfolder, no answer key included.

## Persona Prompt Block
**Role:** CS101 Auto-Grader — an automated system similar to the one your coursework already uses.
**Rules:**
- Runs your program with sample inputs and checks exact output, including decimal places, punctuation, and spacing.
- Any uncaught exception (crash) is an automatic fail for that test case.
- Tests edge cases (boundary values, the "or" branch that's easy to forget), not just the obvious happy path.
- Hard-tier exercises are graded on whether the logic actually generalizes, not just whether it works for one sample input.

## Easy
1. Write a script that reads `movie_rating` (int, input) and prints `"Kid-friendly"` if it's 3 or higher, otherwise `"Not for kids"`.
2. Write a script that reads `club_member_years` (int, input) and sets `discount = 15` if 5 or more years, otherwise `discount = 0`; print the result.
3. Write a script with a multi-branch `if/elif/else` that reads `grade_percent` (int, input) and prints `"A"` for 90+, `"B"` for 80-89, `"C"` for 70-79, and `"F"` otherwise.

## Medium
4. Write a script using `or` that prints `"Lucky number!"` if a user-entered number is `7`, `13`, or `21`, otherwise `"Just a number."`.
5. Write a script using `and` that prints `"Approved"` only if `age` (input, int) is 18 or older AND the user answered `'yes'` to having an ID, otherwise `"Denied"`.
6. Write a script with several **independent** `if` statements (not `elif`) that reads `product_price` (input, float) and prints each message that applies: `"Eligible for free shipping"` if price > 50, `"Eligible for member discount"` if price > 100, `"Premium item"` if price > 200 — more than one message can print for the same input.
7. Write a script with a nested `if` inside an `if/else`: read whether it's raining and whether the user has an umbrella (both compared against `'yes'`); if raining, print a different message depending on the umbrella; if not raining, print one message regardless.

## Hard
8. Write a program checking a small hard-coded inventory dictionary (item name → stock count) against a user-entered item name, with a nested `if/else` inside an outer membership check — first write a version with **intentionally broken/inconsistent indentation** as a comment, then the corrected, working version below it.
9. Write a program that reads three separate input integers and, using only `if`/`elif`/`else` (no `min()`, `max()`, or `sorted()`), determines and prints the **median** (middle value) of the three.
10. Write a program that reads a city name (input) and looks it up in a hard-coded dictionary of city populations; if found, use a nested `if` to print `"Large city"` (population > 1,000,000) or `"Small city"` otherwise; if not found in the dictionary, print `"Unknown city"`.
