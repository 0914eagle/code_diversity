
def get_min_colors(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if s[i] == ')':
            dp[i] = 1
        elif s[i] == '(':
            dp[i] = 2
        else:
            dp[i] = dp[i + 1]
        if i < n - 1 and s[i] == '(' and s[i + 1] == ')':
            dp[i] = min(dp[i], dp[i + 2] + 1)
    return dp[0]

