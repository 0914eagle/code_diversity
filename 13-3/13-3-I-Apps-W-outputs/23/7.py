
def find_min_path_sum(grid):
    # Initialize the dp array with the values from the grid
    dp = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]

    # Fill in the dp array
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] += min(dp[i-1][j], dp[i][j-1])

    # Return the last value of the dp array
    return dp[-1][-1]

