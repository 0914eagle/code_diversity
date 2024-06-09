
def solve(n, m, b, mod, a):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(j - a[i - 1], j + 1):
                if k >= 0 and dp[i - 1][k]:
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= mod
    return dp[n][m]

