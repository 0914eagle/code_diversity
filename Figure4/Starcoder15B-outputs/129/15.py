def minPath(grid, k):
    
    N = len(grid)
    dp = [[[float('inf')] * (k + 1) for _ in range(N)] for _ in range(N)]
    dp[0][0][1] = grid[0][0]
    for i in range(N):
        for j in range(N):
            for l in range(1, k + 1):
                if i > 0:
                    dp[i][j][l] = min(dp[i][j][l], dp[i - 1][j][l - 1] + grid[i][j])
                if j > 0:
                    dp[i][j][l] = min(dp[i][j][l], dp[i][j - 1][l - 1] + grid[i][j])
    return dp[N - 1][N - 1][k]


