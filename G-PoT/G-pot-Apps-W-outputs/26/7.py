
n, t = map(int, input().split())
times = [int(input()) for _ in range(n)]

mod = 998244353

dp = [0] * (t + 1)
dp[0] = 1

for x in times:
    new_dp = [0] * (t + 1)
    prefix_sum = 0
    for i in range(1, t + 1):
        prefix_sum += dp[i - 1]
        if i - x - 1 >= 0:
            prefix_sum -= dp[i - x - 1]
        new_dp[i] = prefix_sum % mod
    dp = new_dp

result = 0
for i in range(1, t + 1):
    result += dp[i]
    result %= mod

result = (result * pow(t, n, mod)) % mod
print(result)
