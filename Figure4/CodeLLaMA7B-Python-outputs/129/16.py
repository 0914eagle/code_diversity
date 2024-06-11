def minPath(grid, k):
    
    n = len(grid)
    m = len(grid[0])
    if k > n*m:
        return []
    if k == 0:
        return []
    if k == 1:
        return [min(grid[0])]
    if k == 2:
        return [min(grid[0]), min(grid[1])]
    if k == n*m:
        return [grid[i][j] for i in range(n) for j in range(m)]

    dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
    dp[0][0] = [grid[0][0], 0]
    for i in range(1, n):
        dp[i][0] = [dp[i-1][0][0], dp[i-1][0][1]+1]
    for j in range(1, m):
        dp[0][j] = [dp[0][j-1][0], dp[0][j-1][1]+1]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = [min(dp[i-1][j][0], dp[i][j-1][0]), min(dp[i-1][j][1]+1, dp[i][j-1][1]+1)]

    res = []
    i = n-1
    j = m-1
    while k > 0:
        res.append(dp[i][j][0])
        if dp[i][j][1] == dp[i][j-1][1]+1:
            j -= 1
        elif dp[i][j][1] == dp[i-1][j][1]+1:
            i -= 1
        k -= 1
    return res


if __name__ == "__main__":
    print(minPath([[1,2,3], [4,5,6], [7,8,9]], 3))
    print(minPath([[5,9