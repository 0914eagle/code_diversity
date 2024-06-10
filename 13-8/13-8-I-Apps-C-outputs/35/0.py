
def get_max_points(n, T, p, t, d):
    # Initialize the dp table with 0 points and no tasks
    dp = [[0, []] for _ in range(n+2)]
    
    # Loop through each location
    for i in range(n+2):
        # Loop through each task at the current location
        for j in range(n):
            # If the task has no deadline or the current location is the starting location, or the task can be completed within the time limit
            if d[j] == -1 or i == 0 or t[j] <= T:
                # Update the dp table with the maximum points and tasks
                if dp[i][0] < dp[j][0] + p[j]:
                    dp[i][0] = dp[j][0] + p[j]
                    dp[i][1] = dp[j][1] + [j+1]
    
    # Return the maximum points and tasks
    return dp[n+1][0], dp[n+1][1]

def get_input():
    n, T = map(int, input().split())
    p = []
    t = []
    d = []
    for i in range(n):
        p_i, t_i, d_i = map(int, input().split())
        p.append(p_i)
        t.append(t_i)
        d.append(d_i)
    return n, T, p, t, d

def main():
    n, T, p, t, d = get_input()
    max_points, tasks = get_max_points(n, T, p, t, d)
    print(max_points)
    print(" ".join(map(str, tasks)))

if __name__ == '__main__':
    main()

