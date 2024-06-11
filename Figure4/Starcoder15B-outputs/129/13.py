def minPath(grid, k):
    
    n = len(grid)
    if n == 1:
        return [grid[0][0]]
    if k == 1:
        return [min(grid[0])]

    # dp[i][j][k] is the minimum path from (i, j) to the end of the grid
    # with length k
    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j][1] = grid[i][j]

    for i in range(n):
        for j in range(n):
            for l in range(2, k + 1):
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < n and 0 <= y < n:
                        dp[i][j][l] = min(dp[i][j][l], dp[x][y][l - 1] + grid[i][j])

    res = [float('inf')] * k
    for i in range(n):
        for j in range(n):
            if dp[i][j][k] < res[0]:
                res = [dp[i][j][k]] + [grid[i][j]]
            elif dp[i][j][k] == res[0]:
                res = min(res, [dp[i][j][k]] + [grid[i][j]], key=lambda x: x[1:])
    return res[1:]


