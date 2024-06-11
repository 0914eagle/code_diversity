def minPath(grid, k):
    
    n = len(grid)
    if n == 1:
        return grid[0]
    if k == 1:
        return [min(grid[0])]

    # dp[i][j][k] = min path from (i, j) to (n - 1, n - 1) with k steps
    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j][1] = grid[i][j]

    for step in range(2, k + 1):
        for i in range(n):
            for j in range(n):
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        dp[i][j][step] = min(dp[i][j][step], dp[ni][nj][step - 1] + grid[i][j])

    return dp[0][0][k]


if