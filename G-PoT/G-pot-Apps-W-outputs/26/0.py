
n, t = map(int, input().split())
times = [int(input()) for _ in range(n)]

mod = 998244353

dp = [0] * (t + 1)
dp[0] = 1

for x in times:
    new_dp = dp.copy()
    for i in range(t, x - 1, -1):
        new_dp[i] += new_dp[i - x]
        new_dp[i] %= mod
    dp = new_dp

total_ways = sum(dp)
result = (total_ways * pow(t, n, mod)) % mod
print(result)
