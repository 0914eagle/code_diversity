
def solve(grid, k):
    # Initialize the dp array with all zeros
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]

    # Initialize the first column with the values from the grid
    for i in range(len(grid)):
        dp[i][0] = grid[i][0]

    # Initialize the first row with the values from the grid
    for j in range(len(grid[0])):
        dp[0][j] = grid[0][j]

    # Fill in the dp array using the recurrence relation
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = dp[i - 1][j] ^ dp[i][j - 1]

    # Return the number of paths with xor sum equal to k
    return dp[len(grid) - 1][len(grid[0]) - 1] == k

