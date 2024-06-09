
def longest_subsequence(b):
    n = len(b)
    dp = [1] * (n + 1)
    for i in range(1, n):
        for j in range(i):
            if b[i] - b[j] == b[j] - b[j - 1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

