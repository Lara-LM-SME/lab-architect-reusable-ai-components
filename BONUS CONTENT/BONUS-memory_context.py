from typing import Dict, List


ROLE_TASKS: Dict[str, List[str]] = {
    "engineer": [
        "Create engineering accounts",
        "Add to engineering Slack channels",
        "Share engineering onboarding doc",
    ],
    "designer": [
        "Create design tools accounts",
        "Add to design Slack channels",
        "Share design system guide",
    ],
}


class Planner:
    """Reusable planner that creates a plan from a type → tasks mapping."""

    def __init__(self, tasks_by_type: Dict[str, List[str]], type_name: str) -> None:
        self.tasks_by_type = tasks_by_type
        self.type_name = type_name

    def create_plan(self, goal: str) -> List[str]:
        tasks = self.tasks_by_type.get(self.type_name, [])
        return [f"{task} for: {goal}" for task in tasks]


class Memory:
    """Simple JSON-like memory store for logging steps and results."""

    def __init__(self) -> None:
        self._entries: List[Dict[str, str]] = []

    def add_memory(self, text: str) -> None:
        self._entries.append({"text": text})

    def get_context(self, query: str) -> str:
        matches = [entry["text"] for entry in self._entries if query in entry["text"]]
        return " | ".join(matches) if matches else ""


class Executor:
    """Executor that pretends to run onboarding steps and returns status messages."""

    def execute_step(self, step: str) -> str:
        return f"[ONBOARDING EXECUTOR] Completed: {step}"


def run_onboarding_helper_with_memory(goal: str, role_type: str) -> None:
    """Run the onboarding helper and record steps/results in memory."""
    planner = Planner(tasks_by_type=ROLE_TASKS, type_name=role_type)
    memory = Memory()
    executor = Executor()

    header = f"Onboarding plan for: {goal} (role: {role_type})"
    print(header)
    print("-" * len(header))

    plan = planner.create_plan(goal)

    for step in plan:
        context = memory.get_context(step)
        result = executor.execute_step(step)
        memory.add_memory(f"Step: {step} | Result: {result}")

        print(f"- Step:    {step}")
        print(f"  Context: {context or '(none yet)'}")
        print(f"  Result:  {result}")
        print()

    print("Final onboarding memory entries (JSON-like):")
    for entry in memory._entries:
        print(f"  {entry}")

    slack_context = memory.get_context("Slack")
    print("\nContext lookup for 'Slack':")
    print(slack_context or "(no entries found)")


if __name__ == "__main__":
    role_type = "engineer"
    goal = f"Onboard new {role_type}"

    run_onboarding_helper_with_memory(goal=goal, role_type=role_type)
