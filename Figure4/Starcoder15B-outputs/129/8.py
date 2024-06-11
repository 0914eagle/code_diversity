def minPath(grid, k):
    
    n = len(grid)
    dp = [[[float('inf')] * (n * n + 1) for _ in range(n)] for _ in range(n)]
    dp[0][0][1] = grid[0][0]
    for i in range(n):
        for j in range(n):
            for l in range(1, n * n + 1):
                if i > 0:
                    dp[i][j][l] = min(dp[i][j][l], dp[i - 1][j][l - 1] + grid[i][j])
                if j > 0:
                    dp[i][j][l] = min(dp[i][j][l], dp[i][j - 1][l - 1] + grid[i][j])
    ans = []
    i, j, l = n - 1, n - 1, k
    while l > 0:
        if i > 0 and dp[i][j][l] == dp[i - 1][j][l - 1] + grid[i][j]:
            ans.append(grid[i][j])
            i -= 1
        elif j > 0 and dp[i][j][l] == dp[i][j - 1][l - 1] + grid[i][j]:
            ans.append(grid[i][j])
            j -= 1
        l -= 1
    ans.append(grid[0][0])
    return ans[::-1]


