
def solve(tasks):
    # Initialize the processor clock and the set of running tasks
    clock = 0
    running_tasks = set()

    # Loop until all tasks are completed
    while len(running_tasks) > 0:
        # Identify running tasks
        running_tasks = {task for task in tasks if task["start"] <= clock and not task["completed"]}

        # Determine the current priorities of the running tasks and which of the running tasks are blocked
        blocked_tasks = set()
        for task in running_tasks:
            # Check if the next instruction is a lock or unlock instruction
            if task["instructions"][0] in ["L", "U"]:
                # Get the resource being locked or unlocked
                resource = int(task["instructions"][1])

                # Check if the resource is already owned or if at least one other task owns a resource with a higher priority ceiling
                if task["instructions"][0] == "L" and (resource in task["owned_resources"] or any(task["priority_ceiling"] >= task2["priority"] for task2 in running_tasks if task2 is not task and resource in task2["owned_resources"])):
                    blocked_tasks.add(task)

        # Update the current priorities of the running tasks
        for task in running_tasks:
            # Get the current priority of the task
            task["priority"] = max(task["base_priority"], min(task["priority_ceiling"], task["priority"]))

        # Execute the next instruction of the non-blocked running task with the highest current priority
        if len(running_tasks) > 0:
            running_tasks = sorted(running_tasks, key=lambda x: x["priority"], reverse=True)
            task = running_tasks[0]
            instruction = task["instructions"][0]

            # Check if the instruction is a compute instruction
            if instruction == "C":
                # Increment the processor clock by one microsecond
                clock += 1

            # Check if the instruction is a lock or unlock instruction
            elif instruction in ["L", "U"]:
                # Get the resource being locked or unlocked
                resource = int(task["instructions"][1])

                # Lock or unlock the resource
                if instruction == "L":
                    task["owned_resources"].add(resource)
                else:
                    task["owned_resources"].remove(resource)

            # Remove the instruction from the task's instruction list
            task["instructions"] = task["instructions"][1:]

            # Check if the task has completed execution
            if len(task["instructions"]) == 0:
                task["completed"] = True

    # Return the completion times of the tasks
    return [task["start"] + task["duration"] for task in tasks]

