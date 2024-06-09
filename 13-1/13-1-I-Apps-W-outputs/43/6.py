
def brutality(hits, k):
    n = len(hits)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i == 1:
                dp[j][i] = hits[i - 1]
            else:
                dp[j][i] = max(dp[j][i - 1], dp[j - 1][i - 1] + hits[i - 1])
    return dp[k][n]

