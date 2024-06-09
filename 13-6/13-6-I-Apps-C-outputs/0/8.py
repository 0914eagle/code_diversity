
def get_maximum_points(n, T, p, t, d, graph):
    # Initialize the maximum points and the tasks to perform
    max_points = 0
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if d[i] != -1:
            # Calculate the time needed to complete the task
            time_needed = t[i] + d[i]
        else:
            # If there is no deadline, the task can be completed immediately
            time_needed = 0
        
        # Loop through each location
        for j in range(n+2):
            # Check if the task can be performed at the current location
            if time_needed <= T - t[j]:
                # Calculate the points that can be earned by performing the task at the current location
                points = p[i]
                
                # Check if the points are higher than the current maximum
                if points > max_points:
                    # Update the maximum points and the tasks to perform
                    max_points = points
                    tasks = [i]
                # Check if the points are equal to the current maximum
                elif points == max_points:
                    # Add the task to the list of tasks to perform
                    tasks.append(i)
    
    # Sort the tasks by their indices
    tasks.sort()
    
    # Return the maximum points and the tasks to perform
    return max_points, tasks

