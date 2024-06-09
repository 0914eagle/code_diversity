
def get_max_value(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], dp[i - 1] + arr[i])
    return dp[n]

