
def get_max_divisible_by_3(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = dp[i]
        if s[i] == '3':
            dp[i + 1] += 1
        if i > 0 and s[i] == '1' and s[i - 1] == '3':
            dp[i + 1] += 1
    return dp[n]

