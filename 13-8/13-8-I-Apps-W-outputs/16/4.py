
def get_maximum_score(arr, k, z):
    n = len(arr)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == 1:
                dp[i][j] = arr[i-1]
            elif j == 1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + arr[i-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + arr[i-1], dp[i-2][j-2] + arr[i-1] + arr[i-2])
    return dp[n][k]

