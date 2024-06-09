
import math

def count_sequences(N, K):
    mod = 1000000007
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
    return dp[N][K]

N, K = map(int, input().split())
print(count_sequences(N, K))

