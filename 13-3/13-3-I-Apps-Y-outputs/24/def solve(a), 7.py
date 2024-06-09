
def solve(a):
    n = len(a)
    dp = [-1] * n
    dp[0] = 0
    for i in range(n):
        for j in range(i+1, min(n, i+a[i]+1)):
            if a[j] % 2 != a[i] % 2:
                dp[j] = max(dp[j], dp[i]+1)
        for j in range(max(0, i-a[i]), i):
            if a[j] % 2 != a[i] % 2:
                dp[j] = max(dp[j], dp[i]+1)
    return dp

