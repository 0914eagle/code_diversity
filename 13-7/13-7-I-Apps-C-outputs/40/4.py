
def simulate_tasks(tasks):
    # Initialize the processor clock and the set of running tasks
    clock = 0
    running_tasks = []

    # Loop until all tasks have completed
    while len(running_tasks) > 0 or len(tasks) > 0:
        # Identify running tasks
        running_tasks = [task for task in running_tasks if task["start"] <= clock and len(task["instructions"]) > 0]

        # Determine the current priorities of the running tasks and which of the running tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            if task["instructions"][0] == "lock":
                resource = task["instructions"][0][1]
                if resource in blocked_tasks or any(task["priority"] < task["ceiling"] for task in running_tasks if task["instructions"][0][1] in task["resources"]):
                    blocked_tasks.append(task)

        # Execute the next instruction of the non-blocked running task (if any) with the highest current priority
        if len(running_tasks) > 0 and len(blocked_tasks) == 0:
            task = max(running_tasks, key=lambda x: x["priority"])
            instruction = task["instructions"].pop(0)
            if instruction == "compute":
                clock += 1
            elif instruction.startswith("lock"):
                resource = instruction[1]
                task["resources"].add(resource)
            elif instruction.startswith("unlock"):
                resource = instruction[1]
                task["resources"].remove(resource)

        # Increment the processor clock by one microsecond
        clock += 1

    # Return the completion times of the tasks
    return [task["start"] + task["duration"] for task in tasks]

