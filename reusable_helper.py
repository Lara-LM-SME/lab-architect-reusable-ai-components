## run python reusable_helper.py in the terminal
from agent_components_ANSWER_KEY import Planner, Memory, Executor
## from agent_components import Planner, Memory, Executor
from role_tasks import ROLE_TASKS


def run_onboarding_helper(role_type: str) -> None:
    planner = Planner()
    memory = Memory()
    executor = Executor()

    goal = f"Onboard new {role_type}"
    print(f"Goal: {goal}")

    # Simple plan from ROLE_TASKS (extension / prep, not core lab requirement)
    task_templates = ROLE_TASKS.get(role_type, [])
    if task_templates:
        steps = [f"{task} for {goal}" for task in task_templates]
    else:
        steps = planner.create_plan(goal)

    print("Plan:", steps)

    print("\nExecuting steps:")
    for step in steps:
        result = executor.execute_step(step)
        memory.add_memory(f"Step: {step} | Result: {result}")
        print("-", result)

    print("\nContext for query:", role_type)
    print(memory.get_context(role_type))

if __name__ == "__main__":
    run_onboarding_helper("engineer")
    
# Outputs:
# /architect_agent_components_lab$ python reusable_helper.py
# Goal: Onboard new engineer
# Plan: ['Create engineering accounts for Onboard new engineer', 'Add to engineering Slack channels for Onboard new engineer', 'Share engineering onboarding doc for Onboard new engineer']

# Executing steps:
# - [EXECUTOR] Completed: Create engineering accounts for Onboard new engineer
# - [EXECUTOR] Completed: Add to engineering Slack channels for Onboard new engineer
# - [EXECUTOR] Completed: Share engineering onboarding doc for Onboard new engineer

# Context for query: engineer
# Step: Create engineering accounts for Onboard new engineer | Result: [EXECUTOR] Completed: Create engineering accounts for Onboard new engineer | Step: Add to engineering Slack channels for Onboard new engineer | Result: [EXECUTOR] Completed: Add to engineering Slack channels for Onboard new engineer | Step: Share engineering onboarding doc for Onboard new engineer | Result: [EXECUTOR] Completed: Share engineering onboarding doc for Onboard new engineer