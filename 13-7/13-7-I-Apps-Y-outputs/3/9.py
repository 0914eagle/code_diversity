
def solve(grid, k):
    n, m = len(grid), len(grid[0])
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[n][m] = 1
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            dp[i][j] += dp[i+1][j]
            if j < m-1 and grid[i][j] ^ grid[i][j+1] == k:
                dp[i][j] += dp[i][j+1]
            if i < n-1 and grid[i][j] ^ grid[i+1][j] == k:
                dp[i][j] += dp[i+1][j]
    return dp[0][0]

