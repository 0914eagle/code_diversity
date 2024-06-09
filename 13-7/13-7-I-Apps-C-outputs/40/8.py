
def solve(tasks):
    # Initialize the processor clock and the current priorities of the tasks
    clock = 0
    priorities = [task[1] for task in tasks]

    # Run the infinite loop until all tasks complete
    while True:
        # Identify the running tasks
        running_tasks = [task for task in tasks if task[0] <= clock and len(task[2]) > 0]

        # Determine the current priorities of the running tasks and which tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            if task[2][0] == "L":
                resource = int(task[2][1])
                if resource in blocked_tasks or any(priorities[task] < priorities[other_task] for other_task in blocked_tasks if other_task[3][resource] > priorities[task]):
                    blocked_tasks.append(task)
            elif task[2][0] == "U":
                resource = int(task[2][1])
                if task in blocked_tasks:
                    blocked_tasks.remove(task)

        # Execute the next instruction of the non-blocked running task with the highest current priority
        if len(blocked_tasks) == 0:
            running_tasks.sort(key=lambda x: x[1])
            task = running_tasks[-1]
            instruction = task[2].pop(0)
            if instruction == "C":
                clock += 1
            elif instruction == "L":
                resource = int(instruction[1])
                task[3][resource] = task[1]
            elif instruction == "U":
                resource = int(instruction[1])
                task[3][resource] = 0

        # If all tasks have completed, return the completion times
        if len(tasks) == 0:
            return [task[0] + clock for task in tasks]

