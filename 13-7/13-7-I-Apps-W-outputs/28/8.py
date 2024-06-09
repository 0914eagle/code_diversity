
def get_maximum_comfort(A):
    n = len(A)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
    return dp[n]
