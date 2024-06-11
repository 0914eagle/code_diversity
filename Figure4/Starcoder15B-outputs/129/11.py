def minPath(grid, k):
    
    N = len(grid)
    if k == 1:
        return [min(min(grid))]
    if k == N * N:
        return [grid[i][j] for i in range(N) for j in range(N)]
    # dp[i][j][k] = min path from (i, j) to the end of the grid with length k
    dp = [[[float('inf')] * (k + 1) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j][1] = grid[i][j]
    for i in range(N):
        for j in range(N):
            for l in range(2, k + 1):
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < N and 0 <= y < N:
                        dp[i][j][l] = min(dp[i][j][l], dp[x][y][l - 1] + grid[i][j])
    return dp[0][0][k]


