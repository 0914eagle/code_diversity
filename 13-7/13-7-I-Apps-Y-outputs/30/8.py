
def solve(s, t):
    n = len(s)
    m = len(t)
    if n == 0 or m == 0:
        return 0
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if s[j] == t[i - 1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return n - dp[m]

