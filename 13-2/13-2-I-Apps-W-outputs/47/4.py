
def solve(s, a):
    n = len(s)
    mod = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(27)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, 27):
            if s[i-1] == chr(j+96):
                dp[j][i] = (dp[j][i-1] + dp[j-1][i-1]) % mod
            else:
                dp[j][i] = dp[j][i-1]
    ans = 0
    max_len = 0
    min_sub = n+1
    for i in range(n+1):
        for j in range(1, 27):
            if dp[j][i] > 0 and a[j-1] >= i:
                ans = (ans + dp[j][i]) % mod
                max_len = max(max_len, i)
                min_sub = min(min_sub, dp[j][i])
    return [ans, max_len, min_sub]

