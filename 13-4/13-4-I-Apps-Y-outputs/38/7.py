
def solve(a, f):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], dp[i - 1] + f[a[i] - 1])
    return dp[n]

