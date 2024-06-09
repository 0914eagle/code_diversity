
def max_value_of_m(a, k):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(n):
        dp[0][i] = a[i]
    for i in range(1, k + 1):
        for j in range(i):
            for l in range(n):
                r = l + i
                if r > n:
                    break
                dp[i][l] = max(dp[i][l], dp[j][l] + dp[i - j - 1][r])
    return max(dp[k])

