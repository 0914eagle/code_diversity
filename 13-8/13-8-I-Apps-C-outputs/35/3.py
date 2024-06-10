
def get_max_points(n, T, tasks):
    # Initialize the maximum points and the tasks to perform
    max_points = 0
    tasks_to_perform = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if tasks[i][2] != -1:
            # Calculate the time left to complete the task
            time_left = T - tasks[i][2]
        else:
            # If there is no deadline, set the time left to the total time
            time_left = T
        
        # Check if the task can be completed within the time left
        if time_left >= tasks[i][1]:
            # Add the points to the maximum points
            max_points += tasks[i][0]
            # Add the task to the list of tasks to perform
            tasks_to_perform.append(i+1)
    
    # Return the maximum points and the list of tasks to perform
    return max_points, tasks_to_perform

def get_optimal_path(n, T, tasks, graph):
    # Initialize the maximum points and the tasks to perform
    max_points = 0
    tasks_to_perform = []
    
    # Loop through each task
    for i in range(n):
        # Check if the task has a deadline
        if tasks[i][2] != -1:
            # Calculate the time left to complete the task
            time_left = T - tasks[i][2]
        else:
            # If there is no deadline, set the time left to the total time
            time_left = T
        
        # Check if the task can be completed within the time left
        if time_left >= tasks[i][1]:
            # Add the points to the maximum points
            max_points += tasks[i][0]
            # Add the task to the list of tasks to perform
            tasks_to_perform.append(i+1)
    
    # Return the maximum points and the list of tasks to perform
    return max_points, tasks_to_perform

def main():
    # Read the input
    n, T = map(int, input().split())
    tasks = []
    for i in range(n):
        tasks.append(list(map(int, input().split())))
    graph = []
    for i in range(n+2):
        graph.append(list(map(int, input().split())))
    
    # Calculate the maximum points and the optimal path
    max_points, tasks_to_perform = get_max_points(n, T, tasks)
    optimal_path = get_optimal_path(n, T, tasks, graph)
    
    # Print the maximum points and the list of tasks to perform
    print(max_points)
    print(" ".join(map(str, tasks_to_perform)))

if __name__ == '__main__':
    main()

