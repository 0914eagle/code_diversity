
def longest_arithmetic_sequence(b):
    n = len(b)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i):
            if b[i - 1] - b[j - 1] == b[j - 1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

