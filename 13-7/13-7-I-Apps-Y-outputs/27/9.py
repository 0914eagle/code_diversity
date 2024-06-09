
def get_maximum_sum(a, k, x):
    n = len(a)
    if n < k or x == 0:
        return -1
    if x == 1:
        return max(a)
    if k == 1:
        return sum(a[:x])
    if x == n:
        return sum(a)

    # dynamic programming
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i < k:
            dp[i] = a[i - 1]
        else:
            dp[i] = max(a[i - 1] + dp[i - k], dp[i - 1])
    return dp[n]

