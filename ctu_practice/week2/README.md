# Week 2 — Conditionals — Theory Questions

Original questions about the concepts practiced in [the Week 2 code exercises](CODE_EXERCISES.md). Explain your reasoning in your own words; no code submission is required for these questions.

## Persona Prompt Block
**Role:** Python code reviewer checking whether your decisions cover every case.
**Rules:**
- Explain which conditions are true and which branch runs, especially at boundaries.
- Treat indentation as part of the program's logic, not just its appearance.
- Give a reason for your choice of `if`, `elif`, `else`, `and`, or `or`.

## Questions

### Easy
1. What happens when an `if` condition is false and the program has an `else` block?
2. In a grade ladder using `if`/`elif`/`else`, why does the order of the checks matter?
3. What is the difference between `>=` and `>` at the exact boundary value, such as a price of `50`?

### Medium
4. Compare `number == 7 or number == 13` with `number == 7 or 13`. Which expression correctly checks the two possible values, and why?
5. An approval requires someone to be at least 18 **and** have an ID. Explain the result for all four combinations of the two conditions (age requirement met or not; ID present or not).
6. Why might three independent `if` statements print multiple messages for one price, while an `if`/`elif`/`else` chain prints at most one?
7. For a rainy-day decision, explain how a nested `if` can check for an umbrella only when it is raining. What does indentation tell Python about which condition owns the inner check?

### Hard
8. An inventory dictionary contains `{"apples": 0}`. Why does checking whether `"apples"` is a key answer a different question from checking whether its stock count is greater than zero? Describe the decisions needed for an unknown item, an out-of-stock item, and an in-stock item.
9. You need the median of three integers using only conditional branches. Describe the comparisons that establish which value is in the middle, including a case where two values are equal. How would you check that no input ordering was missed?
10. A city lookup first checks whether a name exists in a dictionary, then classifies its population. Explain why reversing those checks can cause an error, and describe the branch taken for an unknown city, a city with exactly 1,000,000 people, and a city above that number.

---
Answers are withheld. Save your explanations in your own subfolder and open a pull request when you want a teammate to review them, following [the repository instructions](../../instructions.md).
