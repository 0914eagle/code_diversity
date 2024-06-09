
def solve(n, T, p, t, d, graph):
    # Initialize the maximum points and the tasks to perform
    max_points = 0
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
                # Check if completing the task is optimal
                if points > max_points:
                    # Update the maximum points and the tasks to perform
                    max_points = points
                    tasks = [i]
                # Check if completing the task is suboptimal but still better than the current maximum
                elif points == max_points:
                    # Add the task to the list of tasks to perform
                    tasks.append(i)
        # Check if the task does not have a deadline
        else:
            # Calculate the points earned from completing the task
            points = p[i]
            # Check if completing the task is optimal
            if points > max_points:
                # Update the maximum points and the tasks to perform
                max_points = points
                tasks = [i]
            # Check if completing the task is suboptimal but still better than the current maximum
            elif points == max_points:
                # Add the task to the list of tasks to perform
                tasks.append(i)
    
    # Return the maximum points and the tasks to perform
    return max_points, tasks

