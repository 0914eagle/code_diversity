
import sys

MOD = 998244353

def solve(n, t, times):
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(t + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            if j >= times[i - 1]:
                dp[i][j] = (dp[i][j] + dp[i][j - times[i - 1]]) % MOD

    result = 0
    for i in range(1, n + 1):
        for j in range(t - times[i - 1] + 1):
            result = (result + dp[i - 1][j] * dp[n - i][t - j - 1]) % MOD

    return (result * pow(t, n, MOD)) % MOD

if __name__ == "__main__":
    n, t = map(int, input().split())
    times = [int(input()) for _ in range(n)]

    result = solve(n, t, times)
    print(result)
