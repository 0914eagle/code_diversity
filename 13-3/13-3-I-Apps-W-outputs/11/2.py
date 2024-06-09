
def get_max_value(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])
    return dp[n]

