# Architect Your Agent's Components – Ungraded Lab

## Goal

In this lab you’ll progressively shape a tiny but realistic agent by fixing three core components and then wiring them together. First you correct a `Planner` so it turns a goal into a simple plan (a list of steps), then you fix a `Memory` so it stores text entries and returns sensible context, and an `Executor` so it outputs a clear result for each step. Next you write plain-English “test logic” statements that describe what each method must accept and return, like you would before writing unit tests. Finally, you run a small reusable helper that uses your components end-to-end, and optionally refactor it into a different helper (for example, a meal planner) to see how the same contracts support multiple use cases.

---

## Quick Start

1. **Create & activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS / Linux
   # OR on Windows (PowerShell):
   # .venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Open the student notebook**

   - Open `Reusable_Agent_Components.ipynb` in the Lab, VS Code or Jupyter.
   - Work through Tasks 1–5 in order.

---

## What You Need to Do

### Task 1–3: Fix the component contracts (in the notebook)

In `Architect_Agent_Components_Student.ipynb`:

- **Task 1 – Planner**
  - Fix the `create_plan` method so it returns a **list of step texts** for the given `goal`.
  - In the scaffold, the local variable is already correct; your job is to fix the `return` value.

- **Task 2 – Memory**
  - Fix `add_memory` so it does **not** return a value (Python will return `None`).
  - Fix `get_context` so it returns a **text value** (string), not a number.

- **Task 3 – Executor**
  - Fix `execute_step` so it returns a **result text** that includes the original `step`.

- **Task 4 – Reflection**
  - Write one plain-English rule per component:
    - What must go in?
    - What must come out?

### Task 5: Wire the components together (helper)

- In the last notebook cell you’ll see `run_onboarding_helper(role_type: str)`.
- It uses:
  - `Planner` to build a plan,
  - `Executor` to run each step,
  - `Memory` to log what happened.

When Tasks 1–3 are fixed, running this cell should:

- Print the **goal**
- Show the **plan** (list of steps)
- Print each **executed step**

---

## Moving Code into `agent_components.py`

After completing Tasks 1–3:

1. Open `agent_components.py`.
2. Copy your final versions of:
   - `Planner`
   - `Memory`
   - `Executor`
3. Make sure the file only contains the three class definitions (no extra test code).

This file represents your **reusable agent components**.

---

## Reusable Helper Script

You can also run the helper from a regular Python script:

- `reusable_helper.py` uses:

  ```python
  from agent_components import Planner, Memory, Executor
  from role_tasks import ROLE_TASKS
  ```

- `role_tasks.py` contains example onboarding tasks for different roles.

To see everything working together from the terminal:

```bash
python reusable_helper.py
```

You should see:

- The onboarding goal
- A plan (steps)
- Each step being “executed”
- A simple context string returned from `Memory`

---

## Optional Extension

Think about how you could refactor the reusable helper code to fit a different use case.