
def get_task_priority(task, blocked_tasks):
    # Calculate the current priority of the task
    current_priority = task["base_priority"]
    for blocked_task in blocked_tasks:
        if blocked_task["resource"] == task["resource"]:
            current_priority = max(current_priority, blocked_task["priority"])
    return current_priority

def get_blocked_tasks(task, tasks):
    # Find all tasks that block the current task
    blocked_tasks = []
    for other_task in tasks:
        if other_task["resource"] == task["resource"] and other_task["priority"] > task["priority"]:
            blocked_tasks.append(other_task)
    return blocked_tasks

def execute_task(task, tasks, resources):
    # Execute the next instruction of the task
    instruction = task["instructions"][task["current_instruction"]]
    if instruction[0] == "C":
        # Compute instruction
        task["current_instruction"] += 1
    elif instruction[0] == "L":
        # Lock instruction
        resource = instruction[1]
        if resources[resource] is None:
            # Resource is available, lock it
            resources[resource] = task
            task["current_instruction"] += 1
        else:
            # Resource is already locked, block the task
            task["blocked_tasks"].append(resources[resource])
    elif instruction[0] == "U":
        # Unlock instruction
        resource = instruction[1]
        if resources[resource] == task:
            # Resource is owned by the task, unlock it
            resources[resource] = None
            task["current_instruction"] += 1
        else:
            # Resource is not owned by the task, do nothing
            pass
    return task

def run_tasks(tasks):
    # Initialize the resources and the clock
    resources = [None] * len(tasks)
    clock = 0
    
    # Run the tasks until all tasks have completed
    while True:
        # Identify running tasks
        running_tasks = [task for task in tasks if task["start_time"] <= clock and task["current_instruction"] < len(task["instructions"])]
        
        # Determine the current priorities of the running tasks and which of the running tasks are blocked
        for task in running_tasks:
            task["priority"] = get_task_priority(task, get_blocked_tasks(task, running_tasks))
        
        # Execute the next instruction of the non-blocked running task (if any) with the highest current priority
        running_tasks.sort(key=lambda x: x["priority"], reverse=True)
        for task in running_tasks:
            if len(task["blocked_tasks"]) == 0:
                execute_task(task, tasks, resources)
                break
        
        # Increment the clock by one microsecond
        clock += 1
        
        # Check if all tasks have completed
        if all([task["current_instruction"] == len(task["instructions"]) for task in tasks]):
            break
    
    # Return the time when each task completes
    return [task["start_time"] + task["current_instruction"] for task in tasks]

