
def count_paths(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[m-1][n-1] = 1

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if grid[i][j] == '#':
                continue
            dp[i][j] += dp[i+1][j]
            if j < n-1:
                dp[i][j] += dp[i+1][j+1]

    return dp[0][0]

