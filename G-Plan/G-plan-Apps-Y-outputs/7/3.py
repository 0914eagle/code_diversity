
def min_cost_to_obtain_set(n, k, s):
    if k > 2 ** n:
        return -1

    dp = [[-1] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        dp[i][0] = 0
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            for l in range(1, i + 1):
                cost = i - l
                if dp[i - l][j - 1] != -1:
                    if dp[i][j] == -1 or dp[i][j] > dp[i - l][j - 1] + cost:
                        dp[i][j] = dp[i - l][j - 1] + cost

    return dp[n][k]


if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    result = min_cost_to_obtain_set(n, k, s)
    print(result)
