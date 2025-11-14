# Architect Your Agent's Components — Lab Starter

This folder contains the starter files for the **"Architect Your Agent's Components"** ungraded lab.

## Files

- `agent_components.py` – The file learners will edit. It contains empty `Planner`, `Memory`, and `Executor` classes.
- `ANSWER_KEY_agent_components.py` – **Model solution** showing one valid set of method signatures and docstrings. This file is ignored by Git via `.gitignore` so learners do not see it when cloning.
- `.gitignore` – Configured to ignore virtual environments, build artifacts, and any file with `ANSWER_KEY` in its name.

## Learner Instructions (Summary)

In `agent_components.py`:

1. In the `Planner` class, add a `create_plan(self, goal: str) -> list[str]` method with a one-sentence docstring.
2. In the `Memory` class, add:
   - `add_memory(self, text: str) -> None`
   - `get_context(self, query: str) -> str`
   Each with a one-sentence docstring.
3. In the `Executor` class, add `execute_step(self, step: str) -> str` with a one-sentence docstring.
4. Ensure the file runs without syntax errors.

Implementation details of how these components work internally are **out of scope** for this lab; the focus is on clean, typed interfaces and concise docstrings.

## Quick Start to run this locally:
git clone <your-repo-url>.git
cd <your-repo-folder>
python3 -m venv .venv
source .venv/bin/activate 
python -m pip install --upgrade pip