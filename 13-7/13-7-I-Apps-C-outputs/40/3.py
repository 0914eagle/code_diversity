
def solve(tasks):
    # Initialize the processor clock to 0
    clock = 0
    # Initialize the current priorities of the tasks
    current_priorities = [task[1] for task in tasks]
    # Initialize the blocked tasks
    blocked_tasks = []
    # Initialize the owned resources
    owned_resources = [False] * len(tasks)
    # Loop until all tasks have completed
    while True:
        # Identify the running tasks
        running_tasks = [task for task in tasks if task[0] <= clock]
        # Determine the current priorities of the running tasks
        for task in running_tasks:
            # If the task is blocked, set its current priority to 0
            if task in blocked_tasks:
                current_priorities[task[2]] = 0
            # Otherwise, set its current priority to its base priority
            else:
                current_priorities[task[2]] = task[1]
        # Determine which tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            # If the task is blocked, add it to the blocked tasks list
            if task[3][0] == "L" and (owned_resources[int(task[3][1]) - 1] or any(current_priorities[task[2]] < current_priorities[i] for i in range(len(tasks)) if owned_resources[i])):
                blocked_tasks.append(task)
        # Execute the next instruction of the non-blocked running task with the highest current priority
        if running_tasks and not blocked_tasks:
            task = max(running_tasks, key=lambda x: current_priorities[x[2]])
            instruction = task[3][0]
            if instruction == "C":
                clock += 1
            elif instruction == "L":
                owned_resources[int(task[3][1]) - 1] = True
            elif instruction == "U":
                owned_resources[int(task[3][1]) - 1] = False
            task[3] = task[3][1:]
        # If all tasks have completed, return the completion times
        if not any(task[0] <= clock for task in tasks):
            return [task[0] + clock for task in tasks]

