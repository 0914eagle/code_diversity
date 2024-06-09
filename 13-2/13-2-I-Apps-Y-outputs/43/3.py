
def solve(s, t):
    n = len(s)
    m = len(t)
    dp = [0] * (n + 1)
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i + 1] = max(dp[i + 1], dp[i] + 1)
    return n - dp[n]

