
def get_max_points(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = max(dp[i + 1], dp[i + 2] + min(arr[i], arr[i + 1]))
    return dp[0]

