def minPath(grid, k):
    
    n = len(grid)
    m = len(grid[0])
    if k > n * m:
        return []

    # dp[i][j][k] means the minimum path of length k from (i, j)
    dp = [[[float('inf')] * (k + 1) for _ in range(m)] for _ in range(n)]
    dp[0][0][1] = grid[0][0]

    for i in range(1, n):
        dp[i][0][1] = dp[i - 1][0][1] + grid[i][0]

    for j in range(1, m):
        dp[0][j][1] = dp[0][j - 1][1] + grid[0][j]

    for i in range(1, n):
        for j in range(1, m):
            for k in range(2, k + 1):
                dp[i][j][k] = min(dp[i - 1][j][k - 1] + grid[i][j],
                                  dp[i][j - 1][k - 1] + grid[i][j])

    return [grid[i][j] for i, j, k in sorted(
        [(i, j, dp[i][j][k]) for i in range(n) for j in range(m) for k in range(1, k + 1)],
        key=lambda x: x[2])][:k]
