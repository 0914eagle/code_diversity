
def get_max_points(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = max(dp[i + 1], arr[i] + dp[i + 2])
    return dp[0]

