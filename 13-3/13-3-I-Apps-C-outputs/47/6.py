
def solve(n, levels):
    # Initialize the dp table with the completion time for each level when using item 0
    dp = [levels[i][0] for i in range(n)]

    # Loop through each level
    for i in range(n):
        # Loop through each item
        for j in range(1, n+1):
            # If the completion time for the level when using item j is less than the current minimum time, update the minimum time
            if levels[i][j] < dp[i]:
                dp[i] = levels[i][j]

    # Return the minimum time to beat all levels
    return sum(dp)

