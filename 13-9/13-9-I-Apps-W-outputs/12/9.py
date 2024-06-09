
def solve(n, k, d):
    mod = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i - j >= 0 and j >= d:
                dp[i] += dp[i - j]
        dp[i] %= mod
    return dp[n]

