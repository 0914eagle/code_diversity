
def scavenger_hunt(n, T, tasks, travel_times):
    # Initialize the maximum number of points to be obtained
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks_to_perform = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if tasks[i][2] != -1:
            # Calculate the time required to complete the task and the time required to travel to the task
            task_time = tasks[i][1]
            travel_time = travel_times[i][n+1]
            # Check if the task can be completed within the deadline
            if task_time + travel_time <= tasks[i][2]:
                # Add the points earned by completing the task to the maximum number of points
                max_points += tasks[i][0]
                # Add the task to the list of tasks to be performed
                tasks_to_perform.append(i+1)
    
    # Return the maximum number of points and the list of tasks to be performed
    return max_points, tasks_to_perform

