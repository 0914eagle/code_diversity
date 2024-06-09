
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
            if any(instruction["type"] == "lock" and (instruction["resource"] in blocked_tasks or any(task["priority"] < task2["priority"] for task2 in blocked_tasks)) for instruction in task["instructions"]):
                blocked_tasks.append(task)
        
        # Execute the next instruction of the non-blocked running task (if any) with the highest current priority
        if running_tasks:
            # Sort the running tasks by current priority in descending order
            running_tasks.sort(key=lambda x: x["priority"], reverse=True)
            
            # Execute the next instruction of the highest priority task
            task = running_tasks[0]
            instruction = task["instructions"][0]
            if instruction["type"] == "compute":
                # Execute a compute instruction
                clock += 1
            elif instruction["type"] == "lock":
                # Lock a resource
                task["resources"].add(instruction["resource"])
            elif instruction["type"] == "unlock":
                # Unlock a resource
                task["resources"].remove(instruction["resource"])
            
            # Remove the executed instruction from the task
            task["instructions"] = task["instructions"][1:]
        
        # Increment the processor clock by one microsecond
        clock += 1
    
    # Return the completion times of the tasks
    return [task["start"] + task["duration"] for task in tasks]

