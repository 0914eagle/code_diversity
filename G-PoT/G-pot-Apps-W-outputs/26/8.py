
import sys

MOD = 998244353

def solve(n, t, times):
    dp = [0] * (t + 1)
    dp[0] = 1

    for x in times:
        new_dp = [0] * (t + 1)
        prefix_sum = [0] * (t + 1)
        prefix_sum[0] = dp[0]
        for i in range(1, t + 1):
            prefix_sum[i] = (prefix_sum[i - 1] + dp[i]) % MOD

        for i in range(t + 1):
            new_dp[i] = (prefix_sum[i] - prefix_sum[max(0, i - x)]) % MOD

        dp = new_dp

    result = 0
    for i in range(1, t + 1):
        result = (result + dp[i]) % MOD

    return (result * pow(t, n, MOD)) % MOD

if __name__ == "__main__":
    n, t = map(int, input().split())
    times = [int(input()) for _ in range(n)]

    result = solve(n, t, times)
    print(result)
