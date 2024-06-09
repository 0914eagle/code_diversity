
n, t = map(int, input().split())
times = [int(input()) for _ in range(n)]

mod = 998244353

dp = [0] * (t + 1)
dp[0] = 1

for x in times:
    new_dp = dp.copy()
    for i in range(x, t + 1):
        new_dp[i] += dp[i - x]
        new_dp[i] %= mod
    dp = new_dp

result = dp[t]
for i in range(1, n):
    result = (result * t) % mod

print(result)
