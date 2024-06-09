
def get_max_cost(arr, m, k):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(i, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j - 1], arr[j - 1] - k + (j - i + 1) // m)

    return dp[0][n]

