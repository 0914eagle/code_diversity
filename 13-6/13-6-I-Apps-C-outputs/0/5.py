
def solve(n, T, tasks, travel_times):
    # Initialize the maximum points to be 0
    max_points = 0
    # Initialize the list of tasks to be performed
    tasks_to_perform = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if tasks[i][2] != -1:
            # Calculate the time left to complete the task
            time_left = T - tasks[i][2]
        else:
            # If there is no deadline, set the time left to the total time available
            time_left = T
        
        # Check if the task can be completed within the time left
        if time_left >= tasks[i][1]:
            # If the task can be completed, add its points to the maximum points
            max_points += tasks[i][0]
            # Add the task to the list of tasks to perform
            tasks_to_perform.append(i+1)
            # Subtract the time taken to complete the task from the total time available
            T -= tasks[i][1]
    
    # Return the maximum points and the list of tasks to perform
    return max_points, tasks_to_perform

