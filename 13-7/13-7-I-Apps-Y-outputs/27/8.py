
def get_max_sum_of_reposted_pictures(a, k, x):
    n = len(a)
    if n < k or x == 0:
        return -1
    if k == 1:
        return sum(a[:x])
    if x == 1:
        return max(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i >= k:
            dp[i] = max(dp[i - 1], dp[i - k] + a[i - 1])
        else:
            dp[i] = dp[i - 1] + a[i - 1]
    return dp[n]

