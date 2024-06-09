
def solve(tasks):
    # Initialize the processor clock and the list of running tasks
    clock = 0
    running_tasks = []
    
    # Loop until all tasks are completed
    while tasks:
        # Identify running tasks
        running_tasks = [task for task in tasks if task["start"] <= clock and not all(instruction["type"] == "compute" for instruction in task["instructions"])]
        
        # Determine the current priorities of the running tasks and which of the running tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            # Check if the task is blocked by any other task
            for other_task in running_tasks:
                if other_task is not task and task["instructions"][0]["type"] == "lock" and other_task["instructions"][0]["type"] == "lock" and other_task["instructions"][0]["resource"] == task["instructions"][0]["resource"]:
                    blocked_tasks.append(other_task)
                    break
        
        # Determine the current priority of each running task
        for task in running_tasks:
            task["current_priority"] = max(task["base_priority"], max(other_task["current_priority"] for other_task in blocked_tasks))
        
        # Execute the next instruction of the non-blocked running task (if any) with the highest current priority
        if running_tasks:
            running_task = max(running_tasks, key=lambda x: x["current_priority"])
            instruction = running_task["instructions"][0]
            if instruction["type"] == "compute":
                clock += 1
            elif instruction["type"] == "lock":
                running_task["instructions"].pop(0)
            elif instruction["type"] == "unlock":
                running_task["instructions"].pop(0)
                running_task["current_priority"] = running_task["base_priority"]
        
        # Remove completed tasks from the list of tasks
        tasks = [task for task in tasks if not all(instruction["type"] == "compute" for instruction in task["instructions"])]
    
    # Return the completion times of all tasks
    return [task["start"] + task["instructions"][0]["time"] for task in tasks]

