
def max_points(a):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = max(dp[i + 1], dp[i + 2] + a[i])
    return dp[0]

