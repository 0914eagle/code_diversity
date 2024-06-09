
def get_min_colors(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == ")":
            j = i - 2
            while j >= 0 and s[j] != "(":
                j -= 1
            if j == -1:
                dp[i] = -1
            else:
                dp[i] = max(dp[i], dp[j] + 1)
        else:
            dp[i] = dp[i - 1]
    return dp[n]

