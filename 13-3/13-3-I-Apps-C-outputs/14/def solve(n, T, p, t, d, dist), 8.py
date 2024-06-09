
def solve(n, T, p, t, d, dist):
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
            if time_left >= 0:
                # Calculate the points earned from completing the task
                points = p[i]
                # Check if the points earned are more than the current maximum
                if points > max_points:
                    # Update the maximum points
                    max_points = points
                    # Clear the list of tasks
                    tasks = []
                    # Add the task to the list of tasks
                    tasks.append(i)
                # Check if the points earned are equal to the current maximum
                elif points == max_points:
                    # Add the task to the list of tasks
                    tasks.append(i)
    
    # Sort the list of tasks
    tasks.sort()
    
    # Return the maximum points and the list of tasks
    return max_points, tasks

