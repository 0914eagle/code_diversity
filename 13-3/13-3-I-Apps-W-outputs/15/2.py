
def get_min_colors(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n):
        if s[i] == ')':
            dp[i + 1] = max(dp[i + 1], dp[i] + 1)
        else:
            dp[i + 1] = max(dp[i + 1], dp[i])
    return dp[n]

