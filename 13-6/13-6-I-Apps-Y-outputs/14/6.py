
def get_max_sum(a, k, x):
    n = len(a)
    if n < k or x == 0:
        return -1
    if k == 1:
        return sum(a)
    if x == n:
        return sum(a)
    if x < k:
        return -1
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i < k:
            dp[i] = a[i - 1]
        else:
            dp[i] = max(dp[i - 1], dp[i - k] + a[i - 1])
    return dp[n]

