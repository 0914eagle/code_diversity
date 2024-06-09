
def solve(s, t):
    n = len(s)
    m = len(t)
    if n == m:
        return 0
    elif n > m:
        return n - m
    else:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i):
                if s[i - 1] == t[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - dp[n]

