
def solve(grid, k):
    # Initialize the dp table with all zeros
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]

    # Base case: the xor sum is k if we are at the bottom-right cell
    dp[len(grid) - 1][len(grid[0]) - 1] = 1 if k == 0 else 0

    # Fill in the dp table from the bottom-up
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0]) - 1, -1, -1):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                continue
            dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
            if grid[i][j] != 0:
                dp[i][j] -= dp[i + 1][j + 1] if grid[i][j] ^ k == 0 else 0

    return dp[0][0]

