
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
            if task["instructions"][0] == "L":
                resource = task["instructions"][1]
                if resource in blocked_tasks or any(task["priority"] < task2["priority"] for task2 in blocked_tasks if task2["resource"] == resource):
                    blocked_tasks.append(task)
        
        # Execute the next instruction of the non-blocked running task (if any) with the highest current priority
        if running_tasks:
            running_tasks.sort(key=lambda x: x["priority"], reverse=True)
            task = running_tasks[0]
            instruction = task["instructions"][0]
            if instruction == "C":
                clock += 1
            elif instruction == "L":
                task["resource"] = task["instructions"][1]
                task["priority"] = task["base_priority"]
            elif instruction == "U":
                task["resource"] = None
                task["priority"] = task["base_priority"]
            task["instructions"] = task["instructions"][1:]
            if not task["instructions"]:
                task["completed"] = True
    
    # Return the time each task completes execution
    return [task["start"] + task["duration"] for task in tasks]

