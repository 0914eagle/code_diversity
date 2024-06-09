
def solve(text):
    words = text.split()
    n = len(words)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + len(words[i - 1]) + 1
        for j in range(i - 1, -1, -1):
            if words[i - 1] == words[j]:
                dp[i] = min(dp[i], dp[j] + len(words[i - 1]) + 1)
                break
    return dp[n]

