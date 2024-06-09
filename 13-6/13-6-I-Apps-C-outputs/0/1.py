
def solve(n, T, p, t, d, graph):
    # Initialize the maximum points to be 0
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if d[i] != -1:
            # Calculate the time left to complete the task
            time_left = T - t[i]
            # Check if the task can be completed within the time left
            if time_left >= d[i]:
                # Add the task to the list of tasks to be performed
                tasks.append(i)
                # Update the maximum points
                max_points += p[i]
    
    # Return the maximum points and the list of tasks
    return max_points, tasks

