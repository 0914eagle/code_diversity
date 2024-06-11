def minPath(grid, k):
    
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # n = len(grid)
    # dp = [[0 for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         dp[i][j] = grid[i][j]
    #         if i > 0:
    #             dp[i][j] += dp[i - 1][j]
    #         if j > 0:
    #             dp[i][j] += dp[i][j - 1]
    #         if i > 0 and j > 0:
    #             dp[i][j] -= dp[i - 1][j - 1]
    # return dp[n - 1][n - 1]

    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # n = len(grid)
    # dp = [[0 for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         dp[i][j] = grid[i][j]
    #         if i > 0:
    #             dp[i][j] += dp[i - 1][j]
    #         if j > 0:
    #             dp[i][j] += dp[i][j - 1]
    #         if i > 0 and j > 0:
    #             dp[i][j] -= dp[i - 1][j - 1]
    # return dp[n - 1][n - 1]

    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # n = len(grid)
    # dp = [[0 for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(