
def solve(tasks):
    # Initialize the processor clock and the current priorities of the tasks
    clock = 0
    current_priorities = [task[1] for task in tasks]
    
    # Run the infinite loop until all tasks complete
    while True:
        # Identify the running tasks
        running_tasks = [task for task in tasks if task[0] <= clock and len(task[2]) > 0]
        
        # Determine the current priorities of the running tasks and which tasks are blocked
        blocked_tasks = []
        for task in running_tasks:
            next_instruction = task[2][0]
            if next_instruction[0] == "L":
                resource = int(next_instruction[1])
                if resource in blocked_tasks or any(task[1] >= current_priorities[task_index] for task_index in blocked_tasks):
                    blocked_tasks.append(task_index)
            elif next_instruction[0] == "U":
                resource = int(next_instruction[1])
                if resource in blocked_tasks:
                    blocked_tasks.remove(resource)
        
        # Execute the next instruction of the non-blocked running task with the highest current priority
        if len(running_tasks) > 0:
            running_tasks.sort(key=lambda x: x[1], reverse=True)
            task = running_tasks[0]
            next_instruction = task[2][0]
            if next_instruction[0] == "C":
                clock += 1
            elif next_instruction[0] == "L":
                resource = int(next_instruction[1])
                current_priorities[task[3]] = max(current_priorities[task[3]], task[1])
            elif next_instruction[0] == "U":
                resource = int(next_instruction[1])
                current_priorities[task[3]] = max(current_priorities[task[3]], task[1]) - 1
            task[2].pop(0)
        
        # If all tasks have completed, return the completion times
        if len(tasks) == 0:
            return [task[0] + clock for task in tasks]

