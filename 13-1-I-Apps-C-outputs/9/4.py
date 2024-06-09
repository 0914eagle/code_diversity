
import math

def solve(N, S):
    mod = 1000000007
    dp = [1] * (N + 1)
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            dp[i + 1] += dp[i]
        if i > 0 and S[i - 1] != S[i] and S[i - 1] != S[i + 1]:
            dp[i + 1] += dp[i - 1]
    return dp[N] % mod

