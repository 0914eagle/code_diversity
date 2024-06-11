def minPath(grid, k):
    
    # Initialization
    n = len(grid)
    m = len(grid[0])
    # dp[i][j][k] means the minimum path of length k from the cell (i, j)
    dp = [[[float("inf") for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    # dp[i][j][k] = min(dp[i-1][j][k-1], dp[i][j-1][k-1], dp[i-1][j-1][k-1]) + grid[i][j]
    for i in range(n):
        for j in range(m):
            dp[i][j][1] = grid[i][j]
    # dp[i][j][k] = min(dp[i-1][j][k-1], dp[i][j-1][k-1], dp[i-1][j-1][k-1]) + grid[i][j]
    for k in range(2, k+1):
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j][k] = dp[i][j][k-1]
                elif i == 0:
                    dp[i][j][k] = min(dp[i][j-1][k-1], dp[i][j][k-1]) + grid[i][j]
                elif j == 0:
                    dp[i][j][k] = min(dp[i-1][j][k-1], dp[i][j][k-1]) + grid[i][j]
                else:
                    dp[i][j][k] = min(dp[i-1][j][k-1], dp[i][j-1][k-1], dp[i-1][j-1][k-1]) + grid[i][j]
    return dp[n-1][m-1][k]


if __name__ == "__main__