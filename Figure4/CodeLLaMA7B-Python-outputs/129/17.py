def minPath(grid, k):
    
    n = len(grid)
    m = len(grid[0])
    if k > n*m:
        return []

    # dp[i][j][k] means the minimum path of length k from (i, j)
    dp = [[[float('inf')] * (k+1) for _ in range(m)] for _ in range(n)]
    dp[0][0][1] = grid[0][0]

    for i in range(1, n):
        dp[i][0][1] = dp[i-1][0][1] + grid[i][0]

    for j in range(1, m):
        dp[0][j][1] = dp[0][j-1][1] + grid[0][j]

    for i in range(1, n):
        for j in range(1, m):
            for k in range(2, k+1):
                if k == 2:
                    dp[i][j][k] = min(dp[i-1][j][k], dp[i][j-1][k]) + grid[i][j]
                else:
                    dp[i][j][k] = min(dp[i-1][j][k], dp[i][j-1][k], dp[i-1][j-1][k-1]) + grid[i][j]

    return dp[n-1][m-1][k]


print(minPath([ [1,2,3], [4,5,6], [7,8,9]], 3))
print(minPath([ [5,9,3], [4,1,6], [7,8,2]], 1))
