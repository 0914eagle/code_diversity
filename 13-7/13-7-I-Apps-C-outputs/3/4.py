
def hopper_exploration(arr, d, m):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(i - 1, max(-1, i - d - 1), -1):
            if abs(arr[i - 1] - arr[j]) <= m:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]
