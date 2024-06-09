
def solve(s, t):
    n = len(s)
    m = len(t)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if s[j] == t[i - j - 1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return m - dp[n]

