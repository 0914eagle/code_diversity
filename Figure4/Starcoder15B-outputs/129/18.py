def minPath(grid, k):
    
    n = len(grid)
    if k == 1:
        return [min(grid[0])]
    if k == n * n:
        return [grid[i][i] for i in range(n)]

    # dp[i][j][k] = min path from (i, j) to (n-1, n-1) of length k
    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j][1] = grid[i][j]

    for i in range(n):
        for j in range(n):
            for l in range(2, k + 1):
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        dp[i][j][l] = min(dp[i][j][l], dp[ni][nj][l - 1] + grid[i][j])

    res = [float('inf')] * k
    for i in range(n):
        for j in range(n):
            if dp[i][j][k] < res[0]:
                res = [grid[i][j]] + dp[i][j][1:k]
    return res


