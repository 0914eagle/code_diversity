
def solve(p, m, k):
    n = len(p)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(i - 1, n):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j] + p[j])
    return dp[k][n - 1]

