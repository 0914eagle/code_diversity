
def solve(tasks):
    # Initialize the processor clock and the list of running tasks
    clock = 0
    running_tasks = []
    
    # Loop until all tasks are completed
    while tasks:
        # Identify running tasks
        running_tasks = [task for task in tasks if task["start"] <= clock and not task["completed"]]
        
        # Determine the current priorities of the running tasks and which of the running tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            if task["next_instruction"] == "lock":
                resource = task["next_resource"]
                if resource in task["owned_resources"] or any(task["owned_resources"][resource] >= task["priority"] for task in running_tasks):
                    blocked_tasks.append(task)
        
        # Execute the next instruction of the non-blocked running task with the highest current priority
        if running_tasks and not blocked_tasks:
            task = max(running_tasks, key=lambda x: x["priority"])
            instruction = task["next_instruction"]
            if instruction == "compute":
                clock += 1
            elif instruction == "lock":
                task["owned_resources"][task["next_resource"]] = task["priority"]
            elif instruction == "unlock":
                resource = task["next_resource"]
                task["owned_resources"][resource] = 0
                task["next_instruction"] = "lock" if task["next_resource"] in task["owned_resources"] else "compute"
            task["next_instruction"] = "compute"
        
        # Increment the processor clock by one microsecond
        clock += 1
    
    # Return the completion times of the tasks
    return [task["completion_time"] for task in tasks]

