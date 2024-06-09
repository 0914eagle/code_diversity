
def get_max_value(arr, k):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(n):
        dp[0][i] = arr[i]
    for i in range(1, k + 1):
        for j in range(i):
            for l in range(n - i + 1):
                r = l + i - 1
                dp[i][l] = max(dp[i][l], dp[j][l] + dp[i - j - 1][r + 1] + sum(arr[l:r + 1]))
    return max(dp[k])

