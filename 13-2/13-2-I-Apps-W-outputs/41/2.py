
def solve(p, m, k):
    n = len(p)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(i - 1, n):
            dp[i][j] = max(dp[i - 1][j - 1] + p[j], dp[i][j - 1])
    return dp[k][n - 1]

