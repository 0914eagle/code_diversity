
def solve(n, T, tasks, distances):
    # Initialize the maximum number of points to be obtained
    max_points = 0
    # Initialize the list of tasks to be performed
    task_list = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if tasks[i][2] != -1:
            # Calculate the time required to complete the task
            task_time = tasks[i][1]
            # Check if the task can be completed within the deadline
            if task_time <= tasks[i][2]:
                # Add the task to the list of tasks to be performed
                task_list.append(i)
                # Update the maximum number of points to be obtained
                max_points += tasks[i][0]
    
    # Return the maximum number of points and the list of tasks to be performed
    return max_points, task_list

