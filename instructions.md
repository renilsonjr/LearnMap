# Instructions

How this repository is organized and how to work through it.

## Project and folder structure

1. **Use AI to help design the folder tree.** Ask the AI to help build a topic tree focused on data structures and algorithms, kept language-agnostic (not tied to a specific programming language). Examples of folders that should exist: `array`, `hash_map`, `bubble_sort`, `binary_search`, etc.
2. **Root README.** The main [README.md](README.md) at the project root explains how everything works and how to do the tasks.
3. **Your personal subfolder.** Inside each topic folder (e.g. inside `array/`), create a subfolder named after you (e.g. `frodo/`). This is where all your solution scripts live.

## Generating questions and practicing

1. **Generate the challenges with AI.** For each topic, prompt the AI to act as a testing persona (e.g. a testing platform like grill.me, or a recruiter) and ask it to generate 10 questions ranked by difficulty: 3 easy, 4 medium, 3 hard. The `assessment-generator` agent skill in [.agents/skills/](.agents/skills/) does this automatically.
2. **Document the questions.** The generated material lives in the topic folder: theory questions go in its `README.md`, hands-on coding exercises in `CODE_EXERCISES.md`.
3. **Solve and open a pull request.** Write the code solving the questions inside your personal subfolder. When you finish a topic, open a Pull Request so a teammate can see what you did and review the code.
