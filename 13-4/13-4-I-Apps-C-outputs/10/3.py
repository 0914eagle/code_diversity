
import math

def solve(S):
    mod = 1000000007
    n = len(S)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] * 3) % mod
        if i > 1 and S[i - 2] != S[i - 1]:
            dp[i] = (dp[i] - 1 + mod) % mod
    return dp[n]

