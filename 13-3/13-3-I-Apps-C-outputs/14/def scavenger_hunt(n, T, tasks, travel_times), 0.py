
def scavenger_hunt(n, T, tasks, travel_times):
    # Initialize the maximum points to be 0
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks_to_perform = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if tasks[i][2] != -1:
            # Calculate the time it takes to complete the task and the deadline
            task_time = tasks[i][1]
            deadline = tasks[i][2]
            # Check if the task can be completed within the deadline
            if task_time + deadline <= T:
                # Add the task to the list of tasks to perform
                tasks_to_perform.append(i)
                # Update the maximum points
                max_points += tasks[i][0]
    
    # Return the maximum points and the list of tasks to perform
    return max_points, tasks_to_perform
