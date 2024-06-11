
def count_good_plans(n, m, b, mod, bugs_per_line):
    dp = [[[0 for _ in range(b + 1)] for _ in range(m + 1)] for _ in range(n + 1)
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            for k in range(b + 1):
                dp[i][j][k] = dp[i - 1][j][k]
                if j > 0 and k >= bugs_per_line[i - 1]:
                    dp[i][j][k] += dp[i - 1][j - 1][k - bugs_per_line[i - 1]]
                dp[i][j][k] %= mod

    total_good_plans = sum(dp[n][m][bugs] for bugs in range(b + 1)) % mod
    return total_good_plans

if __name__ == "__main__":
    n, m, b, mod = map(int, input().split())
    bugs_per_line = list(map(int, input().split()))
    result = count_good_plans(n, m, b, mod, bugs_per_line)
    print(result)