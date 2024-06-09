
def solve(n, m, b, mod, a):
    dp = [[0] * (b + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(b + 1):
            for k in range(i):
                if j - a[k] >= 0:
                    dp[i][j] += dp[i - 1][j - a[k]]
            dp[i][j] %= mod
    return dp[n][b]

