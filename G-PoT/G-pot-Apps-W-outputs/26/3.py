
n, t = map(int, input().split())
times = [int(input()) for _ in range(n)]

mod = 998244353

dp = [0] * (t + 1)
dp[0] = 1

for time in times:
    for i in range(t, time - 1, -1):
        dp[i] += dp[i - time]
        dp[i] %= mod

total_ways = dp[t]

for i in range(1, n):
    total_ways = (total_ways * (t - sum(times[:i]))) % mod

result = (total_ways * pow(t, n, mod)) % mod
print(result)
