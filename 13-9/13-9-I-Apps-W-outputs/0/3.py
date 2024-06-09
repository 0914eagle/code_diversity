
def solve(s):
    n = len(s)
    mod = 10 ** 9 + 7
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if s[j] in "wm":
                continue
            dp[i] = (dp[i] + dp[j]) % mod
    return dp[n]

