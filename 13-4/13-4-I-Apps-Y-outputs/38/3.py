
def solve(a, f):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], dp[i - 1] + f[ord(a[i]) - ord('0')])
    return dp[n]

