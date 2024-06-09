
def longest_exploration_sequence(arr, d, m):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i - 1, max(0, i - d - 1), -1):
            if abs(arr[i - 1] - arr[j]) <= m:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

