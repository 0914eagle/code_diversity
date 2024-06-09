
def solve(a):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if a[i - 1] % 2 == 0:
            dp[i] = min(dp[i], dp[i - a[i - 1]] + 1)
        else:
            dp[i] = min(dp[i], dp[i + a[i - 1]] + 1)
    return dp[1:]

