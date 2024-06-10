
def min_cost_to_obtain_set(n, k, s):
    if k > 2 ** n:
        return -1

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + (n - i + 1) if j == 1 else min(dp[i - 1][j - 1], dp[i - 1][j])

    return dp[n][k]

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    print(min_cost_to_obtain_set(n, k, s))
