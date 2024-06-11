def minPath(grid, k):
    
    n = len(grid)
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(n):
        for j in range(n):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
    return dp[n-1][n-1] <= k


