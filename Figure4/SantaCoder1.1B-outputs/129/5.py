def minPath(grid, k):
    
    if not grid:
        return []
    m, n = len(grid), len(grid[0])
    # dp[i][j] = min path of length i to j
    dp = [[float('inf') for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + grid[i][0]
    for j in range(1, n):
        dp[0][j] = min(dp[0][j - 1], dp[1][j]) + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1] - dp[0][0] - dp[m - 1][0] + dp[0][n - 1]


