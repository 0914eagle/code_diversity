
def solve(tasks):
    # Initialize the clock and the set of running tasks
    clock = 0
    running_tasks = set()
    
    # Loop until all tasks are completed
    while len(running_tasks) > 0:
        # Identify running tasks
        running_tasks = {task for task in tasks if task["start"] <= clock and not task["completed"]}
        
        # Determine the current priorities of the running tasks and which tasks are blocked
        blocked_tasks = set()
        for task in running_tasks:
            blocked_tasks.update(task["blocked"])
            task["current_priority"] = max(task["base_priority"], max(task["blocked"], default=0))
        
        # Execute the next instruction of the non-blocked running task with the highest current priority
        running_tasks = sorted(running_tasks, key=lambda x: x["current_priority"], reverse=True)
        for task in running_tasks:
            if len(task["blocked"]) == 0:
                instruction = task["instructions"].pop(0)
                if instruction[0] == "C":
                    clock += 1
                elif instruction[0] == "L":
                    task["blocked"].add(instruction[1])
                elif instruction[0] == "U":
                    task["blocked"].remove(instruction[1])
                break
        
        # Update the clock and check if any tasks have completed
        clock += 1
        for task in tasks:
            if task["start"] + len(task["instructions"]) <= clock and not task["completed"]:
                task["completed"] = True
    
    # Return the completion times of the tasks
    return [task["start"] + len(task["instructions"]) for task in tasks]

