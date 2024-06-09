
import math

def hopscotch(N, X, Y):
    mod = 1000000007
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, X + 1):
                if i - k >= 0 and dp[i - k][j] > 0:
                    dp[i][j] += dp[i - k][j]
            for l in range(1, Y + 1):
                if j - l >= 0 and dp[i][j - l] > 0:
                    dp[i][j] += dp[i][j - l]
            dp[i][j] %= mod
    
    return dp[N][N]

