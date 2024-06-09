
def solve(strings):
    n = len(strings)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if strings[i - 1].startswith(strings[j]) and strings[i - 1].endswith(strings[j]):
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

