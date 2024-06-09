
import math

def solve(N, X, Y):
    mod = 1000000007
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i - X >= 0 and j - Y >= 0:
                dp[i][j] += dp[i - X][j - Y]
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            dp[i][j] %= mod
    
    return dp[N][N]

