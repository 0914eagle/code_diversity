
def find_longest_subsegment(a):
    n = len(a)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if a[i - 1] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]

