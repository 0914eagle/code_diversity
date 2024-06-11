def minPath(grid, k):
    
    n = len(grid)
    dp = [[[float('inf') for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
    dp[0][0][1] = grid[0][0]
    for i in range(n):
        for j in range(n):
            for l in range(1, k + 1):
                if i > 0:
                    dp[i][j][l] = min(dp[i][j][l], dp[i - 1][j][l - 1] + grid[i][j])
                if j > 0:
                    dp[i][j][l] = min(dp[i][j][l], dp[i][j - 1][l - 1] + grid[i][j])
    return dp[n - 1][n - 1][k]

