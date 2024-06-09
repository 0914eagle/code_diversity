
def get_maximum_cost(string, max_changes):
    n = len(string)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if string[i - 1] == "d":
            dp[i] = max(dp[i - 1], dp[i - 2] + 1)
        else:
            dp[i] = max(dp[i - 1], dp[i - 2])
    for i in range(1, n + 1):
        for j in range(1, max_changes + 1):
            if string[i - 1] == "d":
                dp[i] = max(dp[i], dp[i - j - 1] + j)
            else:
                dp[i] = max(dp[i], dp[i - j - 1] + j)
    return dp[n]

