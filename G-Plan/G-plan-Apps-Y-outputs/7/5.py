cost_to_obtain_set(n, k, s):
    if k > 2 ** n:
        return -1

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + i - 1)

    return dp[n][k]

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    result = min_cost_to_obtain_set(n, k, s)
    print(result)
