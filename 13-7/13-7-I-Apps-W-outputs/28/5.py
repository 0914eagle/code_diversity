
def get_maximum_comfort(A):
    N = len(A)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
    return dp[N]

