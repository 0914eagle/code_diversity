
def longest_interesting_subsequence(A, S):
    N = len(A)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(dp[i - 1], 1)
        for j in range(1, K + 1):
            if i - j >= 0 and A[i - j] <= S:
                dp[i] = max(dp[i], dp[i - j] + 1)
    return dp[N]

