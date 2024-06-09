
def solve(s, t):
    n = len(s)
    m = len(t)
    if n == m:
        return 0
    elif n < m:
        return -1
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if s[j] == s[i - 1] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    
    max_len = 0
    for i in range(m):
        max_len = max(max_len, dp[i])
    
    return n - m + max_len

