
def solve(n, T, p, t, d, dist):
    # Initialize the maximum points and the tasks to perform
    max_points, tasks = 0, []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if d[i] != -1:
            # Check if the task can be completed within the deadline
            if d[i] - t[i] <= T:
                # Add the task to the list of tasks to perform
                tasks.append(i)
                # Update the maximum points
                max_points += p[i]
        else:
            # Add the task to the list of tasks to perform
            tasks.append(i)
            # Update the maximum points
            max_points += p[i]
    
    # Return the maximum points and the tasks to perform
    return max_points, tasks

