
def get_max_comfort(a):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] ^ a[i - 1]
    max_comfort = 0
    for i in range(n):
        for j in range(i, n + 1):
            max_comfort = max(max_comfort, dp[j] - dp[i])
    return max_comfort

