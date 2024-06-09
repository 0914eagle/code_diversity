
def hopper_exploration(arr, D, M):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i - 1, max(0, i - D - 1), -1):
            if abs(arr[i - 1] - arr[j]) <= M:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

