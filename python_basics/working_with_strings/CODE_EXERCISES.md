# Working with Strings — Code Exercises

Write real, runnable Python for each item below. Put your solutions in your own subfolder inside this topic folder (e.g. `Frodo/`, `Maverick/`), one script per exercise, then open a PR per [../../instrucoes.MD](../../instrucoes.MD).

## Easy
1. Write a script that concatenates a first and last name into a full name and prints it.
2. Write a function `shout(text)` that returns the text in all uppercase with an exclamation mark appended.
3. Write a function `string_length(s)` that returns the length of a string without using `len()` (loop and count).

## Medium
4. Write a function `last_n_chars(s, n)` using slicing to return the last `n` characters of a string.
5. Write a function `words_from_sentence(sentence)` that splits a sentence into words, then rejoins them with hyphens.
6. Write a function `format_greeting(name, age)` using an f-string to return `"Hi, I'm <name> and I'm <age> years old."`.
7. Write a function `has_valid_extension(filename)` that checks if a filename ends with `.py`, `.txt`, or `.md`.

## Hard
8. Write a function `build_report(rows)` that builds a large string from a list of row strings using `"".join()` instead of `+=` in a loop; comment on why this is more efficient.
9. Write a function `count_unicode_bytes(s)` that encodes a string to UTF-8 and returns both the byte length and the character length, printing both for a string containing an emoji.
10. Write a function `is_palindrome(s)` that returns `True` if `s` is a palindrome, ignoring case, spaces, and punctuation.
