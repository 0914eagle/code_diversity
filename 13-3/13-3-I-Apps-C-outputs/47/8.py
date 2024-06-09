
def solve(n, levels):
    # Initialize the dp table with the completion time for each level when using item 0
    dp = [levels[i][0] for i in range(n)]

    # Loop through each level
    for i in range(n):
        # Loop through each item
        for j in range(1, n+1):
            # If the shortcut item is not the current item
            if levels[i][1] != j:
                # Update the dp table with the minimum completion time for the current level and item
                dp[i] = min(dp[i], dp[i-1] + levels[i][j])

    # Return the minimum completion time for all levels
    return dp[-1]

