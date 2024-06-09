
def solve(a):
    n = len(a)
    dp = [0] * n
    for i in range(n):
        if a[i] % 2 == 0:
            dp[i] = 1
        else:
            dp[i] = -1
    for i in range(n):
        for j in range(i+1, n):
            if a[j] % 2 == a[i] % 2:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp

