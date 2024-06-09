
def count_ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]
    return dp[n]

