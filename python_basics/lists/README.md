# Lists — Practice Questions

## Persona Prompt Block
**Role:** Grill.me-style automated testing platform.
**Rules:**
- Auto-grades against a rubric: correctness, edge cases, and code style.
- Timed mentality — concise, correct answers score higher than long-winded ones.
- Flags any answer that would produce a runtime error if actually executed.
- Hard-tier questions require reasoning about performance or internals, not just syntax.

## Questions

### Easy
1. How do you create an empty list and add one item to it?
2. How do you access the third element of a list?
3. What method removes the last element of a list and returns it?

### Medium
4. What is list slicing, and how would you reverse a list using a slice?
5. What is the difference between `list.sort()` and `sorted(list)`?
6. What is a list comprehension? Rewrite `[x*2 for x in range(5) if x % 2 == 0]` as an equivalent `for` loop.
7. How do you remove duplicates from a list while, as best as possible, preserving order?

### Hard
8. Explain the difference between a shallow copy (`list.copy()` or `list[:]`) and a deep copy (`copy.deepcopy()`) for a list of lists.
9. Why is inserting at the beginning of a Python list (`list.insert(0, x)`) O(n), and what data structure would you use instead for frequent front insertions?
10. Explain the danger of using a mutable default argument like `def f(x, lst=[]):` and how it relates to list identity across function calls.

---
Answers are withheld here. Solve these in your own subfolder and open a PR, per [../../instrucoes.MD](../../instrucoes.MD).
