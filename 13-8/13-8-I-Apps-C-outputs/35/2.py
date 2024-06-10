
def read_input():
    n, T = map(int, input().split())
    tasks = []
    for _ in range(n):
        p, t, d = map(int, input().split())
        tasks.append((p, t, d))
    travel_times = []
    for _ in range(n+2):
        travel_times.append(list(map(int, input().split())))
    return n, T, tasks, travel_times

def get_maximum_points(n, T, tasks, travel_times):
    # Initialize the dp table
    dp = [[0] * (n+2) for _ in range(T+1)]
    # Initialize the tasks to be performed
    tasks_to_perform = [False] * (n+2)
    
    # Populate the dp table
    for t in range(T+1):
        for i in range(n+2):
            if t == 0:
                dp[t][i] = 0
            elif i == n+1:
                dp[t][i] = dp[t-1][i-1]
            else:
                dp[t][i] = max(dp[t-1][i], dp[t-1][i-1] + tasks[i-1][0])
    
    # Find the maximum points that can be obtained
    max_points = 0
    for t in range(T+1):
        for i in range(n+2):
            if dp[t][i] > max_points:
                max_points = dp[t][i]
    
    # Find the tasks to be performed to obtain the maximum points
    for t in range(T+1):
        for i in range(n+2):
            if dp[t][i] == max_points:
                tasks_to_perform[i] = True
    
    return max_points, tasks_to_perform

def print_output(max_points, tasks_to_perform):
    print(max_points)
    for i in range(len(tasks_to_perform)):
        if tasks_to_perform[i]:
            print(i, end=" ")
    print()

if __name__ == '__main__':
    n, T, tasks, travel_times = read_input()
    max_points, tasks_to_perform = get_maximum_points(n, T, tasks, travel_times)
    print_output(max_points, tasks_to_perform)

