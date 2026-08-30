# Type Annotations — Code Exercises

## Persona Prompt Block
**Role:** Senior Engineer reviewing your pull request.
**Rules:**
- Reviews your code like a PR — would this pass review as-is?
- Pushes back on code that technically works but ignores the concept being practiced (e.g. skipping type hints when the exercise is about type hints).
- Checks that comments explaining "why" are present where an exercise asks for an explanation.
- Rewards code that a teammate could read and extend without asking you questions.

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Write a function `add(a: int, b: int) -> int` with full type annotations and call it.
2. Write a script that calls a type-annotated function with the "wrong" type (e.g. a string instead of an int) and shows Python still runs it, proving annotations aren't enforced at runtime.
3. Write a function using `Optional[str]` (or `str | None`) for a parameter that can be missing.

## Medium
4. Write `first_item(items: list[int]) -> int` using built-in generics (3.9+) and an equivalent using `List[int]` from `typing`.
5. Write `find_user(id: int) -> Optional[str]` that returns `None` when not found, plus a caller that correctly checks for `None` before using the result.
6. Annotate a variable directly (e.g. `count: int = 0`) and explain in a comment what this buys you over a plain assignment.
7. Write a small script with an intentional type mismatch, then add a comment describing what `mypy` would report if run on it.

## Hard
8. Write a generic function `first(items: list[T]) -> T` using `TypeVar` that works correctly for a list of ints and a list of strings.
9. Define a `Protocol` called `Sized` with a `__len__` method, then write `describe_size(obj: Sized) -> str` that works with any object implementing `__len__` (e.g. list, str) without inheritance.
10. Write a small module that starts fully untyped, then progressively add annotations to two of its functions; comment on which parts were easy vs. hard to annotate (e.g. functions returning `Any`, complex nested data).
