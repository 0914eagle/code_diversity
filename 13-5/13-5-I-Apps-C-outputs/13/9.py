
import math

def hopscotch(N, X, Y):
    mod = 1000000007
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, int(math.ceil(i / X)) + 1):
                for l in range(1, int(math.ceil(j / Y)) + 1):
                    if k * X <= i and l * Y <= j:
                        dp[i][j] += dp[i - k * X][j - l * Y]
                        dp[i][j] %= mod

    return dp[N][N]

