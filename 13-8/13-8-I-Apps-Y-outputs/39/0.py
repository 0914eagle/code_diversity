
def get_min_shots(a):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = float('inf')
        for j in range(1, i + 1):
            dp[i] = min(dp[i], dp[j - 1] + a[j - 1] * j)
    return dp[n]

