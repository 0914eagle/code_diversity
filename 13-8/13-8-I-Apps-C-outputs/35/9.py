
def get_max_points(n, T, tasks, travel_times):
    # Initialize the dp table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Loop through each task
    for i in range(1, n + 1):
        # Loop through each location
        for j in range(1, n + 1):
            # Check if the task can be performed within the deadline
            if tasks[i][2] == -1 or tasks[i][2] >= travel_times[i][j]:
                # Update the dp table with the maximum points
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + tasks[i][0])
            else:
                # Update the dp table with the maximum points
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
    
    # Find the maximum points
    max_points = max(dp[n])
    
    # Initialize the list of tasks
    tasks_to_do = []
    
    # Loop through each task
    for i in range(n, 0, -1):
        # Check if the task is part of the maximum points
        if dp[i][n] != dp[i - 1][n]:
            # Add the task to the list of tasks to do
            tasks_to_do.append(i)
    
    # Return the maximum points and the list of tasks to do
    return max_points, tasks_to_do

def main():
    # Read the input
    n, T = map(int, input().split())
    tasks = []
    travel_times = []
    for i in range(n):
        tasks.append(list(map(int, input().split())))
        travel_times.append(list(map(int, input().split())))
    
    # Call the function to get the maximum points and tasks to do
    max_points, tasks_to_do = get_max_points(n, T, tasks, travel_times)
    
    # Print the maximum points and tasks to do
    print(max_points)
    print(" ".join(map(str, tasks_to_do)))

if __name__ == '__main__':
    main()

