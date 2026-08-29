# Dictionaries — Practice Questions

## Persona Prompt Block
**Role:** Grill.me-style automated testing platform.
**Rules:**
- Auto-grades against a rubric: correctness, edge cases, and code style.
- Timed mentality — concise, correct answers score higher than long-winded ones.
- Flags any answer that would produce a runtime error if actually executed.
- Hard-tier questions require reasoning about performance or internals, not just syntax.

## Questions

### Easy
1. How do you create a dictionary with two key-value pairs?
2. How do you access the value for a key that might not exist, without raising an error?
3. How do you get all the keys of a dictionary as a list?

### Medium
4. What is the difference between `dict.get(key)` and `dict[key]`?
5. How would you iterate over both keys and values of a dictionary at the same time?
6. What is a dictionary comprehension? Write one that maps numbers 1-5 to their squares.
7. How do you merge two dictionaries in modern Python (3.9+)?

### Hard
8. Explain why dictionary keys must be hashable and immutable, and what happens if you try to use a list as a key.
9. Since Python 3.7, dictionaries preserve insertion order. Explain how this differs from earlier versions and why it matters for reproducibility.
10. Explain how a Python `dict` is implemented under the hood (hash table) and why average-case lookup is O(1) but worst-case can degrade.

---
Answers are withheld here. Solve these in your own subfolder and open a PR, per [../../instrucoes.MD](../../instrucoes.MD).
