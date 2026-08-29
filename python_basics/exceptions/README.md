# Exceptions — Practice Questions

## Persona Prompt Block
**Role:** Grill.me-style automated testing platform.
**Rules:**
- Auto-grades against a rubric: correctness, edge cases, and code style.
- Timed mentality — concise, correct answers score higher than long-winded ones.
- Flags any answer that would produce a runtime error if actually executed.
- Hard-tier questions require reasoning about performance or internals, not just syntax.

## Questions

### Easy
1. What keyword block do you use to catch an exception in Python?
2. What exception is raised when you divide by zero?
3. What does the `finally` block do?

### Medium
4. What's the difference between catching `except Exception:` broadly vs. catching a specific exception like `except ValueError:`?
5. How do you raise a custom exception, and why might you define your own exception class?
6. What is the purpose of the `else` clause in a `try/except/else` block?
7. How would you catch multiple exception types in a single `except` clause?

### Hard
8. Explain exception chaining in Python (`raise ... from ...`) and why it's useful for debugging.
9. Why is using a bare `except:` considered bad practice, and what specific problems can it hide (e.g. swallowing `KeyboardInterrupt`)?
10. Describe the difference between EAFP ("easier to ask forgiveness than permission") and LBYL ("look before you leap") styles in Python, with an example of each for checking a dictionary key.

---
Answers are withheld here. Solve these in your own subfolder and open a PR, per [../../instrucoes.MD](../../instrucoes.MD).
