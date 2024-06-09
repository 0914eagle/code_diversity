
def get_maximum_points(n, T, p, t, d):
    # Initialize the dp table with 0 for all indices
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Loop through each location
    for i in range(1, n + 1):
        # Loop through each time step
        for t in range(T + 1):
            # Check if the current location is the starting location
            if i == 1:
                # If the current time step is 0, set the points to 0
                if t == 0:
                    dp[i][t] = 0
                # If the current time step is greater than 0, set the points to the previous location's points
                else:
                    dp[i][t] = dp[i - 1][t - 1]
            # Check if the current location is the ending location
            elif i == n:
                # If the current time step is less than or equal to the deadline, set the points to the previous location's points plus the current location's points
                if t <= d[i - 1]:
                    dp[i][t] = dp[i - 1][t - 1] + p[i - 1]
                # If the current time step is greater than the deadline, set the points to 0
                else:
                    dp[i][t] = 0
            # Check if the current location is not the starting or ending location
            else:
                # If the current time step is less than or equal to the deadline, set the points to the maximum of the previous location's points plus the current location's points, the previous location's points, and 0
                if t <= d[i - 1]:
                    dp[i][t] = max(dp[i - 1][t - 1] + p[i - 1], dp[i - 1][t], 0)
                # If the current time step is greater than the deadline, set the points to 0
                else:
                    dp[i][t] = 0

    # Return the maximum points and the list of tasks to perform
    return max(dp[n][T]), [i for i in range(1, n + 1) if dp[i][T] == max(dp[n][T])]

