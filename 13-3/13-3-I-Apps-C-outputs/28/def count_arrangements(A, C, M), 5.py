
import sys

def count_arrangements(A, C, M):
    mod = 1000000007
    dp = [[0] * (C+M+1) for _ in range(A+1)]
    dp[0][0] = 1
    for i in range(1, A+1):
        for j in range(1, C+M+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            dp[i][j] %= mod
    return dp[A][C+M]

A, C, M = map(int, input().split())
print(count_arrangements(A, C, M))

