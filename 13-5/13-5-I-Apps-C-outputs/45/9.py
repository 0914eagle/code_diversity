
def get_task_priority(task, current_priorities, blocked_tasks):
    # Calculate the current priority of the task
    task_priority = task["base_priority"]
    for blocked_task in blocked_tasks:
        if blocked_task["resource"] == task["resource"]:
            task_priority = max(task_priority, current_priorities[blocked_task["task_id"]])
    return task_priority

def get_blocked_tasks(tasks, current_priorities, resource):
    # Find all tasks that are blocked by the given resource
    blocked_tasks = []
    for task in tasks:
        if task["resource"] == resource and (task["resource"] in current_priorities or current_priorities[task["task_id"]] >= task["base_priority"]):
            blocked_tasks.append(task)
    return blocked_tasks

def get_next_task(tasks, current_priorities, clock):
    # Find the next task to execute
    next_task = None
    for task in tasks:
        if task["start_time"] <= clock and task["instructions"]:
            if not next_task or current_priorities[task["task_id"]] > current_priorities[next_task["task_id"]]:
                next_task = task
    return next_task

def execute_instruction(task, instruction, current_priorities, clock):
    # Execute the given instruction and update the current priorities and clock
    if instruction[0] == "C":
        clock += 1
    elif instruction[0] == "L":
        current_priorities[task["task_id"]] = get_task_priority(task, current_priorities, get_blocked_tasks(tasks, current_priorities, instruction[1]))
    elif instruction[0] == "U":
        current_priorities[task["task_id"]] = get_task_priority(task, current_priorities, [])
    return clock

def simulate_mars_pathfinder(tasks):
    # Simulate the execution of the tasks using the Priority Ceiling Protocol
    current_priorities = {}
    clock = 0
    for task in tasks:
        current_priorities[task["task_id"]] = task["base_priority"]
    while tasks:
        next_task = get_next_task(tasks, current_priorities, clock)
        if not next_task:
            break
        clock = execute_instruction(next_task, next_task["instructions"].pop(0), current_priorities, clock)
        if not next_task["instructions"]:
            tasks.remove(next_task)
    return clock

if __name__ == '__main__':
    # Example input
    tasks = [
        {"start_time": 50, "base_priority": 2, "resource": 1, "instructions": ["C1", "L1", "C1", "U1", "C1"]},
        {"start_time": 1, "base_priority": 1, "resource": 1, "instructions": ["C1", "L1", "C100", "U1", "C1"]},
        {"start_time": 70, "base_priority": 3, "resource": 1, "instructions": ["C1"]}
    ]
    print(simulate_mars_pathfinder(tasks))

