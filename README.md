# LearnMap

A practice repository for learning programming topics through AI-generated, difficulty-ranked assessments. Each topic folder contains theory questions and hands-on coding exercises in a 3 Easy / 4 Medium / 3 Hard split, graded against a "testing persona" (recruiter, professor, automated grader). Answers are withheld — you solve them in your own subfolder inside each topic folder and open a Pull Request for review.

The full workflow is described in [instructions.md](instructions.md).

## How it works

1. Pick a topic folder and read its **Persona Prompt Block** — it sets how your answers will be judged.
2. Work through the theory questions and coding exercises, easy → hard.
3. Put your solutions in a personal subfolder inside the topic (e.g. `Frodo/`).
4. Open a PR per topic so a teammate can review.

## Tooling

Assessment material is generated and graded with the agent skills in [.agents/skills/](.agents/skills/): `assessment-generator` creates the ranked question/exercise sets, and `study-mode` provides interactive tutoring when you're stuck.

## Road to a master's degree

[`road-to-master.json`](road-to-master.json) defines a prerequisite map for graduate-level preparation in Artificial Intelligence. Degree-style, self-paced courses generated from that map live in [`courses/`](courses/); `courses/MAE111` is the reference implementation.
