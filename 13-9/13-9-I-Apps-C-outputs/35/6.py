
def longest_interesting_subsequence(A, S):
    N = len(A)
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if A[i] - A[j] <= S:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

