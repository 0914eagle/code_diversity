
def solve(n, T, p, t, d, graph):
    # Initialize the maximum points and the tasks to perform
    max_points = 0
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if d[i] != -1:
            # Calculate the time required to complete the task
            time_required = t[i] + graph[i][n+1]
            # Check if the task can be completed within the deadline
            if time_required <= d[i]:
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

