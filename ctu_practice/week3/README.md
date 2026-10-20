# Week 3 — Lists, Tuples, and Loops — Theory Questions

Original questions about the concepts practiced in [the Week 3 code exercises](CODE_EXERCISES.md). Explain your reasoning in your own words; no code submission is required for these questions.

## Persona Prompt Block
**Role:** Python tutor checking how you trace collections and loops.
**Rules:**
- Track the collection, the current item, and any counter or running total separately.
- State when a loop starts, repeats, and stops.
- Consider empty input and boundary cases, not just the usual example.

## Questions

### Easy
1. In a five-item list, which indexes select the first, third, and fifth items? Why does counting indexes start at a different number from counting items?
2. How do a list and a tuple differ when you want to change an element after creating the collection?
3. In `for day in weekdays:`, what does `weekdays` represent, and what does `day` represent on each pass through the loop?

### Medium
4. To calculate an average with a `for` loop, why must a running total be initialized before the loop? What else do you need besides the total before dividing?
5. A `while` loop adds interest until a balance reaches a goal. Explain why checking the goal before each update matters, and what should happen if the starting balance already meets the goal.
6. In a word-entry loop that stops at `done`, where should the sentinel check happen relative to `.append()`? What should the stored list contain if `done` is the first entry?
7. When looping over `stock = {"apples": 3, "pears": 0}`, what do you receive by default on each pass, and how do you obtain the count for the current fruit? Why should the final out-of-stock count be printed after the loop?

### Hard
8. An `n` by `n` multiplication table uses a loop inside another loop. Explain how many times the inner loop runs in total for `n = 4`, why it restarts for each row, and where the newline belongs.
9. A sentence contains letters, digits, spaces, and punctuation. Describe a decision process that counts vowels, consonants, and digits without counting any character twice. How would uppercase vowels affect your checks?
10. A number-entry loop stops at `0` and then computes an average. Explain what goes wrong if `0` is stored or if it is the first input. Describe the checks needed before dividing and before looking for values above the average.

---
Answers are withheld. Save your explanations in your own subfolder and open a pull request when you want a teammate to review them, following [the repository instructions](../../instructions.md).
