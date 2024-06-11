def minPath(grid, k):
    
    n = len(grid)
    if n == 1:
        return [grid[0][0]]
    if k == 1:
        return [min(grid[0])]

    # dp[i][j][k] = min path from (i, j) to (n-1, n-1) of length k
    dp = [[[float('inf')] * (k+1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j][1] = grid[i][j]
    for l in range(2, k+1):
        for i in range(n):
            for j in range(n):
                if i > 0:
                    dp[i][j][l] = min(dp[i][j][l], dp[i-1][j][l-1])
                if j > 0:
                    dp[i][j][l] = min(dp[i][j][l], dp[i][j-1][l-1])
                dp[i][j][l] += grid[i][j]
    return dp[n-1][n-1][k]

