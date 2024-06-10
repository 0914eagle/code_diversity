cost_to_obtain_set(n, k, s):
    dp = [[-1] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + n - s[i - 1].count(s[i - 1]))

    return dp[n][k]


if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    result = min_cost_to_obtain_set(n, k, s)
    print(result)
