def minPath(grid, k):
    
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(n):
        for j in range(n):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
    print(dp)
    path = []
    i, j = n-1, n-1
    while i > 0 or j > 0:
        path.append(grid[i][j])
        if i > 0 and j > 0 and dp[i-1][j] < dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    path.append(grid[0][0])
    path.reverse()
    return path[:k]

