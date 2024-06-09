
def solve(tasks):
    # Initialize the processor clock and the list of running tasks
    clock = 0
    running_tasks = []
    
    # Loop until all tasks are completed
    while tasks:
        # Identify running tasks
        running_tasks = [task for task in tasks if task["start"] <= clock and not all(instruction["type"] == "C" for instruction in task["instructions"])]
        
        # Determine the current priorities of the running tasks and which of the running tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            # Check if the task is blocked by any other task
            for other_task in running_tasks:
                if task is not other_task and task["base_priority"] < other_task["base_priority"]:
                    # Check if the other task owns a resource that this task needs to lock
                    for instruction in task["instructions"]:
                        if instruction["type"] == "L" and instruction["resource"] in other_task["resources"]:
                            blocked_tasks.append(other_task)
                            break
        
        # Execute the next instruction of the non-blocked running task (if any) with the highest current priority
        if running_tasks:
            running_tasks.sort(key=lambda x: x["current_priority"], reverse=True)
            task = running_tasks[0]
            instruction = task["instructions"][0]
            if instruction["type"] == "C":
                # Compute instruction, increment the clock by one microsecond
                clock += 1
            elif instruction["type"] == "L":
                # Lock instruction, add the resource to the task's resources list
                task["resources"].append(instruction["resource"])
            elif instruction["type"] == "U":
                # Unlock instruction, remove the resource from the task's resources list
                task["resources"].remove(instruction["resource"])
            
            # Remove the executed instruction from the task's instructions list
            task["instructions"] = task["instructions"][1:]
        
        # If all instructions have been executed, remove the task from the list of running tasks
        if not task["instructions"]:
            running_tasks.remove(task)
    
    # Return the completion times of all tasks
    return [task["start"] + task["duration"] for task in tasks]

