
n, t = map(int, input().split())
times = [int(input()) for _ in range(n)]

MOD = 998244353

dp = [0] * (t + 1)
dp[0] = 1

for time in times:
    new_dp = dp.copy()
    for i in range(t - time, -1, -1):
        new_dp[i + time] = (new_dp[i + time] + dp[i]) % MOD
    dp = new_dp

result = sum(dp) % MOD
print((result * pow(t, n, MOD)) % MOD)
