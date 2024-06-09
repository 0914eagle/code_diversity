
def get_max_points(n, T, p, t, d, dist):
    # Initialize the dp table with 0 for all indices
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Loop through each location
    for i in range(1, n + 1):
        # Loop through each time step
        for t in range(T + 1):
            # Check if the task at the current location has a deadline
            if d[i - 1] != -1 and t > d[i - 1]:
                # If the deadline has passed, skip this location
                continue

            # Loop through each previous location
            for j in range(i):
                # Check if the task at the previous location has a deadline
                if d[j] != -1 and t - dist[i - 1][j] > d[j]:
                    # If the deadline has passed, skip this location
                    continue

                # Update the dp table with the maximum points
                dp[i][t] = max(dp[i][t], dp[j][t - dist[i - 1][j]] + p[i - 1])

    # Return the maximum points and the indices of the tasks to be performed
    return dp[n][T], [i for i in range(1, n + 1) if dp[i][T] > 0]

