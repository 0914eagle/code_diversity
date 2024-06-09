
def longest_interesting_subsequence(A, S):
    N = len(A)
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i], dp[i - K] + 1)
    return dp[N]

