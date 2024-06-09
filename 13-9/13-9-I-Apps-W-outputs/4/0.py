
def split_strip(strip, s, l):
    n = len(strip)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i - 1, max(-1, i - l - 1), -1):
            if strip[i - 1] - strip[j] <= s:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

