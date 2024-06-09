
def solve(n, m, b, mod, a):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(j+1):
                if dp[i-1][j-k] and k <= a[i-1]:
                    dp[i][j] += dp[i-1][j-k]
    
    total_bugs = sum(a) * m
    if total_bugs > b:
        return 0
    
    return dp[n][m] % mod

