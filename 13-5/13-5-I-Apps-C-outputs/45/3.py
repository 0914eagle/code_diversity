
def get_current_priority(task, blocked_tasks):
    # Calculate the current priority of the task based on its base priority and the priorities of the tasks it blocks
    current_priority = task["base_priority"]
    for blocked_task in blocked_tasks:
        current_priority = max(current_priority, blocked_task["current_priority"])
    return current_priority

def execute_instruction(task, instruction):
    # Execute the instruction and update the task's current priority
    if instruction[0] == "C":
        # Compute instruction, increment the processor clock by 1 microsecond
        task["current_priority"] += 1
    elif instruction[0] == "L":
        # Lock instruction, lock the resource and update the task's current priority
        task["current_priority"] += 1
        task["owned_resources"].append(instruction[1])
    elif instruction[0] == "U":
        # Unlock instruction, unlock the resource and update the task's current priority
        task["current_priority"] -= 1
        task["owned_resources"].remove(instruction[1])
    return task["current_priority"]

def run_tasks(tasks, resources):
    # Initialize the processor clock to 0
    processor_clock = 0
    
    # Initialize the tasks' current priorities and owned resources
    for task in tasks:
        task["current_priority"] = task["base_priority"]
        task["owned_resources"] = []
    
    # Run the tasks in an infinite loop
    while True:
        # Identify the running tasks
        running_tasks = [task for task in tasks if task["start_time"] <= processor_clock and task["current_priority"] > 0]
        
        # Determine the current priorities of the running tasks and which tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            if task["instructions"][0][0] == "L" and (task["owned_resources"] or resources[task["instructions"][0][1]]["priority_ceiling"] >= task["current_priority"]):
                blocked_tasks.append(task)
        
        # Execute the next instruction of the non-blocked running task (if any) with the highest current priority
        if running_tasks and not blocked_tasks:
            task = max(running_tasks, key=lambda x: x["current_priority"])
            task["current_priority"] = execute_instruction(task, task["instructions"].pop(0))
        
        # Increment the processor clock by 1 microsecond if no compute instruction was executed
        if not blocked_tasks:
            processor_clock += 1
        
        # Check if all tasks have completed execution
        if not any(task["current_priority"] > 0 for task in tasks):
            break
    
    # Return the time each task completes execution
    return [task["start_time"] + processor_clock for task in tasks]

