def minPath(grid, k):
    
    n = len(grid)
    # dp[i][j][k] is the min path from (i, j) to the end with k steps
    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j][0] = grid[i][j]
    for i in range(n):
        for j in range(n):
            for step in range(1, k + 1):
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < n:
                        dp[i][j][step] = min(dp[i][j][step], dp[x][y][step - 1])
                dp[i][j][step] += grid[i][j]
    return dp[0][0][k]


