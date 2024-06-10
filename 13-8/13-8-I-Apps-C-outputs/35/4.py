
def get_max_points(n, T, p, t, d, distance):
    # Initialize the dp table with 0 for all indices
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Loop through all possible tasks
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Check if the task is completed within the time limit
            if d[i - 1] == -1 or d[i - 1] >= t[i - 1]:
                # Calculate the maximum points that can be obtained by completing the task
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + p[i - 1])
            # Check if the task is completed within the time limit and the next task is also completed within the time limit
            if d[i - 1] + t[i - 1] <= T and d[j - 1] + t[j - 1] <= T:
                # Calculate the maximum points that can be obtained by completing the task and the next task
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + p[i - 1] + dp[j][j - 1])
    
    # Return the maximum points that can be obtained
    return dp[n][n]

def get_tasks(n, T, p, t, d, distance):
    # Initialize the dp table with 0 for all indices
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    task_list = []

    # Loop through all possible tasks
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Check if the task is completed within the time limit
            if d[i - 1] == -1 or d[i - 1] >= t[i - 1]:
                # Calculate the maximum points that can be obtained by completing the task
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + p[i - 1])
                task_list.append(i)
            # Check if the task is completed within the time limit and the next task is also completed within the time limit
            if d[i - 1] + t[i - 1] <= T and d[j - 1] + t[j - 1] <= T:
                # Calculate the maximum points that can be obtained by completing the task and the next task
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + p[i - 1] + dp[j][j - 1])
                task_list.append(i)
                task_list.append(j)
    
    # Return the list of tasks
    return task_list

def main():
    n, T = map(int, input().split())
    p = list(map(int, input().split()))
    t = list(map(int, input().split()))
    d = list(map(int, input().split()))
    distance = []
    for i in range(n + 2):
        distance.append(list(map(int, input().split())))
    
    max_points = get_max_points(n, T, p, t, d, distance)
    task_list = get_tasks(n, T, p, t, d, distance)
    print(max_points)
    print(" ".join(map(str, task_list)))

if __name__ == '__main__':
    main()

