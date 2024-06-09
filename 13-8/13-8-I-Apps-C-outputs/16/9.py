
def longest_strictly_increasing_subsegment(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

