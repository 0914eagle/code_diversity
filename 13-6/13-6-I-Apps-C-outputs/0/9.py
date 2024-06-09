
def get_maximum_points(n, T, p, t, d, graph):
    # Initialize the maximum points and the tasks to perform
    max_points = 0
    tasks = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if d[i] != -1:
            # Calculate the time it takes to complete the task and the time it takes to travel to the task
            task_time = t[i]
            travel_time = graph[i][n+1]
            
            # Check if the task can be completed within the deadline
            if task_time + travel_time <= d[i]:
                # Add the task to the list of tasks to perform
                tasks.append(i)
                max_points += p[i]
        
    # Return the maximum points and the tasks to perform
    return max_points, tasks

