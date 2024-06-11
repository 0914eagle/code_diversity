def minPath(grid, k):
    
    n = len(grid)
    if n == 1:
        return [grid[0][0]]
    if k == 1:
        return [min(grid[0])]

    # dp[i][j][k] = min path to (i, j) with k steps
    dp = [[[float('inf') for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j][1] = grid[i][j]

    for steps in range(2, k + 1):
        for i in range(n):
            for j in range(n):
                for ni, nj in neighbors(i, j, n):
                    dp[i][j][steps] = min(dp[i][j][steps], dp[ni][nj][steps - 1] + grid[i][j])

    return dp[0][0][k]


