# Week 3 — Lists, Tuples, and Loops — Code Exercises

Original exercises inspired by Week 3 topics (lists, tuples, `while` and `for` loops, sentinel values, nested loops, looping over strings and dictionaries) — not copies of any CTU/zyBooks assignment. Write real, runnable Python for each item; put solutions in your own subfolder, no answer key included.

## Persona Prompt Block
**Role:** CS101 Auto-Grader — an automated system similar to the one your coursework already uses.
**Rules:**
- Runs your program with sample inputs and checks exact output, including decimal places, punctuation, and spacing.
- Any uncaught exception (crash) or loop that never ends is an automatic fail for that test case.
- Tests edge cases: an empty list, a single item, a sentinel typed on the very first input, off-by-one boundaries.
- Hard-tier exercises are graded on whether the logic generalizes to any input size, not just the sample.

## Easy
1. Create a list of five snacks, print the whole list, then print the first, third, and fifth items using their index.
2. Create `steps = [4200, 8100, 6500]`, change the second element to `9000`, append `7300`, then print the list and how many items it holds using `len()`.
3. Create a tuple of the five weekdays `('Mon', 'Tue', 'Wed', 'Thu', 'Fri')` and use a `for` loop to print `"Today is <day>"` for each one.

## Medium
4. Given `ratings = [4.5, 3.0, 5.0, 2.5, 4.0]`, use a `for` loop with an accumulator variable to compute the sum, then print the average formatted to 2 decimal places, plus the lowest and highest rating using `min()` and `max()`.
5. Read a savings `goal` (float, input). Starting from `balance = 500.0`, use a `while` loop that adds 8% interest each year until the balance reaches the goal; print the year number and balance (2 decimals) on every iteration, then the total years it took.
6. Read words from the user one per line until they type `done` (a sentinel value that should not be stored). Store the words in a list with `.append()`, then print how many words were entered and print the words in reverse order using `reversed()`.
7. Given `stock = {'apples': 3, 'pears': 0, 'plums': 7}`, use a `for` loop over the dictionary to print `"<fruit>: <n> in stock"` for each entry; inside the same loop, count how many fruits are out of stock (value `0`) and print that count after the loop ends.

## Hard
8. Read `n` (int, input) and use nested `for` loops with `range()` to print an `n` by `n` multiplication table, one row per line, values separated by spaces (use `end=' '` and an empty `print()` at the end of each row).
9. Read a sentence from the user and use a `for` loop over its characters to count vowels, consonants (letters that are not vowels), and digits separately, ignoring everything else (spaces, punctuation); print the three counts.
10. Read integers into a list until the user enters `0` (the sentinel, not stored). Then, without using `sum()`, use a `for` loop to compute the total and count the even numbers; finally print the average (2 decimals) and, in a second `for` loop, every number in the list that is greater than that average. Handle the case where the user enters `0` immediately (empty list) without crashing.
