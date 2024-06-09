
def solve(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n):
        if s[i] == '3':
            dp[i + 1] = 1
        elif s[i] == '0':
            if i + 1 < n and s[i + 1] == '3':
                dp[i + 2] = 1
        else:
            dp[i + 1] = dp[i]
    return sum(dp)

