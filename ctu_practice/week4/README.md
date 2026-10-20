# Week 4 — Functions — Theory Questions

Original questions about the concepts practiced in [the Week 4 code exercises](CODE_EXERCISES.md). Explain your reasoning in your own words; no code submission is required for these questions.

## Persona Prompt Block
**Role:** Technical interviewer checking whether you can explain a small Python program.
**Rules:**
- Trace what enters a function, what it computes, and what it returns.
- Separate a function's return value from anything printed on the screen.
- Explain bugs using the actual names, values, and scope involved.

## Questions

### Easy
1. What is the difference between defining a function with `def` and calling that function?
2. In `greet(name)`, what is a parameter, and what is an argument when you call `greet("Frodo")`?
3. How do `return` and `print()` differ? What can the caller do with a returned value?

### Medium
4. A `rectangle_area(width, height)` function is called twice with different dimensions. Explain how the same function can produce different results without changing its definition.
5. A `cylinder_volume()` function calls `circle_area()`. Trace the flow of arguments and returned values between the two functions. Why is reusing `circle_area()` helpful?
6. A function calculates `minutes / 60` but omits `return`. What value does the caller receive, and why does the calculation alone not give the caller the answer?
7. A function returns `tax_amount, total_price`, and the caller writes `tax, total = get_order_total(...)`. Explain what is returned and how the two names receive their values.

### Hard
8. A function increments a global visit counter. Explain why assigning to the counter inside the function needs special treatment in Python, and describe one drawback of making the function depend on global state.
9. A function is defined as `calc_Bonus` but called as `calc_bonus`. Explain the error Python raises and how name matching differs from a function returning the wrong numerical answer.
10. A file defines `km_to_miles()` and reads input inside `if __name__ == "__main__":`. Explain what runs when the file is executed directly versus imported by another file, and why that distinction helps someone reuse or test the conversion function.

---
Answers are withheld. Save your explanations in your own subfolder and open a pull request when you want a teammate to review them, following [the repository instructions](../../instructions.md).
