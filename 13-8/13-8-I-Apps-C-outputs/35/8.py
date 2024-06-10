
def get_max_points(n, T, p_list, t_list, d_list, distance_matrix):
    # Initialize the dp table with 0 for all indices
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Loop through all possible tasks
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If the task is not done and there is a deadline, check if the task can be completed within the deadline
            if dp[i][j] == 0 and d_list[j - 1] != -1:
                if d_list[j - 1] - t_list[j - 1] < T:
                    dp[i][j] = 1
    
    # Loop through all possible tasks
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If the task is not done, check if the task can be completed within the time limit
            if dp[i][j] == 0 and t_list[j - 1] <= T:
                dp[i][j] = 1
    
    # Return the maximum total points and the list of tasks to be performed
    max_points = 0
    tasks = []
    for i in range(1, n + 1):
        if dp[n][i] == 1:
            max_points += p_list[i - 1]
            tasks.append(i)
    return max_points, tasks

def get_input():
    n, T = map(int, input().split())
    p_list = []
    t_list = []
    d_list = []
    distance_matrix = []
    for i in range(n):
        p, t, d = map(int, input().split())
        p_list.append(p)
        t_list.append(t)
        d_list.append(d)
        distance_matrix.append(list(map(int, input().split())))
    return n, T, p_list, t_list, d_list, distance_matrix

if __name__ == '__main__':
    n, T, p_list, t_list, d_list, distance_matrix = get_input()
    max_points, tasks = get_max_points(n, T, p_list, t_list, d_list, distance_matrix)
    print(max_points)
    print(" ".join(map(str, tasks)))

