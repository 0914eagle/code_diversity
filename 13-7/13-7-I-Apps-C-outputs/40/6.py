
def solve(tasks):
    # Initialize the clock and the set of running tasks
    clock = 0
    running_tasks = set()
    
    # Loop until all tasks are completed
    while running_tasks:
        # Identify the running tasks
        running_tasks = {task for task in tasks if task["start"] <= clock and not task["completed"]}
        
        # Determine the current priorities of the running tasks and which tasks are blocked
        blocked_tasks = set()
        for task in running_tasks:
            # If the next instruction is to lock a resource, check if it is already owned or if another task has a higher priority ceiling
            if task["instructions"][0] == "L":
                resource = task["instructions"][1]
                if resource in task["owned_resources"] or any(task["priority_ceiling"] >= task["current_priority"] for task in running_tasks if resource in task["owned_resources"]):
                    blocked_tasks.add(task)
        
        # Determine the current priority of each running task
        for task in running_tasks:
            task["current_priority"] = max(task["base_priority"], max(task["current_priority"], task["priority_ceiling"]))
        
        # Execute the next instruction of the non-blocked running task with the highest current priority
        if running_tasks - blocked_tasks:
            task = max(running_tasks - blocked_tasks, key=lambda x: x["current_priority"])
            instruction = task["instructions"].pop(0)
            if instruction == "C":
                clock += 1
            elif instruction.startswith("L"):
                resource = instruction[1]
                task["owned_resources"].add(resource)
            elif instruction.startswith("U"):
                resource = instruction[1]
                task["owned_resources"].remove(resource)
        
        # Increment the clock by one microsecond
        clock += 1
    
    # Return the completion time of each task
    return [task["start"] + task["duration"] for task in tasks]

