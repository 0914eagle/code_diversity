def minPath(grid, k):
    
    # Time Complexity: O(N*N)
    # Space Complexity: O(N*N)
    # N = number of rows in grid
    # M = number of columns in grid
    # N <= M
    # dp[i][j][k] = minimum path of length k from cell (i, j)
    # dp[i][j][k] = min(dp[i-1][j][k-1], dp[i][j-1][k-1], dp[i-1][j-1][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[i][j][k] = min(dp[i][j][k], dp[i][j][k-1])
    # dp[