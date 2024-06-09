
def solve(n, T, p, t, d, graph):
    # Initialize the maximum points to be 0
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if d[i] != -1:
            # Check if the task can be completed within the deadline
            if d[i] - t[i] <= T:
                # Add the task to the list of tasks to be performed
                tasks.append(i)
                # Update the maximum points
                max_points += p[i]
        else:
            # Check if the task can be completed within the time limit
            if t[i] <= T:
                # Add the task to the list of tasks to be performed
                tasks.append(i)
                # Update the maximum points
                max_points += p[i]
    
    # Return the maximum points and the list of tasks
    return max_points, tasks

