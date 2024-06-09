
import math

n, t = map(int, input().split())
times = [int(input()) for _ in range(n)]

mod = 998244353

dp = [0] * (t + 1)
dp[0] = 1

for time in times:
    new_dp = [0] * (t + 1)
    prefix_sum = [0] * (t + 1)
    for i in range(1, t + 1):
        prefix_sum[i] = (prefix_sum[i - 1] + dp[i - 1]) % mod

    for i in range(1, t + 1):
        new_dp[i] = (prefix_sum[i] - prefix_sum[max(0, i - time)]) % mod

    dp = new_dp

result = 0
for i in range(1, t + 1):
    result = (result + dp[i]) % mod

result = (result * pow(math.factorial(n), mod - 2, mod)) % mod
result = (result * pow(t, n, mod)) % mod

print(result)
