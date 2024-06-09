
import math

def count_sequences(N, K):
    mod = 1000000007
    dp = [1] * (N + 1)
    for i in range(2, K + 1):
        for j in range(1, N + 1):
            for k in range(1, j + 1):
                dp[j] += dp[j - k]
                dp[j] %= mod
    return dp[N]

N, K = map(int, input().split())
print(count_sequences(N, K))

