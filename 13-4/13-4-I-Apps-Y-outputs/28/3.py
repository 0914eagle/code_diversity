
def solve(a):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(1, i):
            if a[i - 1] - a[j - 1] == 1:
                dp[i] = min(dp[i], dp[j - 1] + 1)
    return dp[n]

