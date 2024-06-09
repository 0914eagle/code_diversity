
def scavenger_hunt(n, T, p, t, d, dist):
    # Initialize the maximum points to be 0
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if d[i] != -1:
            # Calculate the time it takes to complete the task
            time_taken = t[i] + dist[i][n+1]
            # Check if the task can be completed within the deadline
            if time_taken <= d[i]:
                # Add the points for the task to the maximum points
                max_points += p[i]
                # Add the task to the list of tasks to be performed
                tasks.append(i+1)
    
    # Return the maximum points and the list of tasks
    return max_points, tasks

