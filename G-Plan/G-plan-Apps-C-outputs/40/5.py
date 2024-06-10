
def count_good_plans(n, m, b, mod, a):
    dp = [[[0 for _ in range(b + 1)] for _ in range(m + 1)] for _ in range(n + 1)
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            for k in range(b + 1):
                dp[i][j][k] = dp[i - 1][j][k]
                if j > 0 and k >= a[i - 1]:
                    dp[i][j][k] += dp[i - 1][j - 1][k - a[i - 1]]
                dp[i][j][k] %= mod

    result = sum(dp[n][m][bugs] for bugs in range(b + 1)) % mod
    return result

if __name__ == "__main__":
    n, m, b, mod = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_good_plans(n, m, b, mod, a))
