# Basic Syntax — Practice Questions

## Persona Prompt Block
**Role:** PySyntax Bot — an automated grading platform (Grill.me-style) for Python fundamentals.
**Rules:**
- Every answer is checked for technical precision — vague answers lose points even if "in the right direction."
- Any code you write must be syntactically valid Python 3.
- Partial credit for correct reasoning with a minor slip; zero credit for guessing.
- Hard-tier questions are graded on depth of explanation, not just a correct final answer.

## Questions

### Easy
1. What character do you use to start a single-line comment in Python?
2. How does Python determine code blocks (e.g., inside an `if` statement or function) instead of using curly braces?
3. Is Python case-sensitive? Show that `Variable` and `variable` are treated as different names.

### Medium
4. What is the difference between a statement and an expression in Python? Give one example of each.
5. Why doesn't Python require a semicolon at the end of a line, and what happens if you put one there anyway?
6. What does PEP 8 recommend for line length and indentation, and why does following it matter on a team project?
7. Why does inconsistent indentation inside the same block raise an `IndentationError`? What rule is being violated?

### Hard
8. Explain how mixing tabs and spaces can produce a `TabError` in Python 3, and why the language is strict about this.
9. Walk through how Python handles a multi-line statement using an explicit line continuation (`\`) versus the implicit continuation inside `()`, `[]`, or `{}`.
10. What is the difference between a syntax error and a runtime error? Give an example of Python code that is syntactically valid but fails only when executed with specific input.

---
Answers are withheld here. Solve these in your own subfolder and open a PR, per [../../instrucoes.MD](../../instrucoes.MD).
