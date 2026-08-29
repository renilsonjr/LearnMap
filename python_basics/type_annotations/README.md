# Type Annotations — Practice Questions

## Persona Prompt Block
**Role:** Senior Engineer reviewing your pull request.
**Rules:**
- Evaluates as if reviewing real code — clarity and future maintainability matter as much as correctness.
- Pushes back on hand-wavy typing claims ("just use `Any`") without justification.
- Rewards awareness of tooling (`mypy`/`pyright`) and real migration tradeoffs.
- Marks down answers that ignore backward-compatibility concerns.

## Questions

### Easy
1. How do you annotate a function's parameter and return type in Python (e.g. a function that adds two ints)?
2. Do type annotations in Python get enforced at runtime by default?
3. What module historically provided types like `List`, `Dict`, and `Optional` for annotations (pre-3.9)?

### Medium
4. What is the difference between `list[int]` and `List[int]`, and when did the built-in generics become available?
5. What does `Optional[str]` mean, and how does it relate to `Union[str, None]`?
6. What tool would you use to statically check type annotations without running the code (e.g. `mypy`)?
7. How do you annotate a variable — not just a function — with a type hint?

### Hard
8. Explain how `TypeVar` is used to write a generic function that works with multiple types while preserving type relationships.
9. What is a `Protocol` in Python's typing system, and how does it enable structural typing ("duck typing" with static checks)?
10. Discuss the tradeoffs of adding type annotations to a large existing dynamically-typed codebase — what benefits and what migration challenges arise?

---
Answers are withheld here. Solve these in your own subfolder and open a PR, per [../../instrucoes.MD](../../instrucoes.MD).
