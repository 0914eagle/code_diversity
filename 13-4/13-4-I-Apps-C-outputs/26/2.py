
import math

def solve(N, K):
    mod = 1000000007
    dp = [1] * (N + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, N + 1):
        for j in range(1, K + 1):
            dp[i] += dp[i - 1]
        dp[i] %= mod

    return dp[N]

