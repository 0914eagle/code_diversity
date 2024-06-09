
def longest_interesting_subsequence(A, S):
    N = len(A)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(dp[i - 1], 1)
        for j in range(1, i):
            if A[i - 1] + A[j - 1] <= S:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[N]

