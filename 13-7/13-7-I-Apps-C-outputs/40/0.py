
def priority_ceiling_protocol(tasks):
    # Initialize the processor clock to zero
    clock = 0
    
    # Initialize the current priorities of the tasks
    current_priorities = [task[1] for task in tasks]
    
    # Initialize the blocked tasks
    blocked_tasks = []
    
    # Run the infinite loop
    while True:
        # Identify the running tasks
        running_tasks = [task for task in tasks if task[0] <= clock and len(task[2]) > 0]
        
        # Determine the current priorities of the running tasks and which tasks are blocked
        for task in running_tasks:
            # Get the next instruction in the task
            instruction = task[2][0]
            
            # Check if the instruction is a compute instruction
            if instruction[0] == "C":
                # Execute the compute instruction
                task[0] += 1
                
                # Update the current priority of the task
                current_priorities[task[3]] = max(current_priorities[task[3]], task[1])
                
            # Check if the instruction is a lock instruction
            elif instruction[0] == "L":
                # Get the resource being locked
                resource = instruction[1]
                
                # Check if the resource is already owned by another task
                if any(task[3] != task_idx and task[2][0][1] == resource for task_idx, task in enumerate(running_tasks)):
                    # Block the task
                    blocked_tasks.append(task[3])
                    
                    # Update the current priority of the task
                    current_priorities[task[3]] = max(current_priorities[task[3]], task[1])
                    
        # Execute the next instruction of the non-blocked running task with the highest current priority
        running_tasks = [task for task in running_tasks if task[3] not in blocked_tasks]
        if len(running_tasks) > 0:
            running_tasks.sort(key=lambda x: x[3])
            task = running_tasks[-1]
            instruction = task[2].pop(0)
            if instruction[0] == "C":
                task[0] += 1
            elif instruction[0] == "L":
                pass
            elif instruction[0] == "U":
                pass
            
        # Increment the processor clock
        clock += 1
        
        # Check if all tasks have completed execution
        if all(len(task[2]) == 0 for task in tasks):
            break
    
    # Return the completion times of the tasks
    return [task[0] for task in tasks]

