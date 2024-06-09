
def get_max_value(arr, k):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(n + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = dp[i - 1][j - 1] + arr[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i - 1])
    for _ in range(k):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1])
    return dp[n][n]

