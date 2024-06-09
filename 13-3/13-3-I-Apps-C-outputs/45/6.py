
import sys

def solve(N, A, B):
    mod = 1000000007
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        dp[i] = (dp[i-1] + A[i-1]) % mod
        if i > 1:
            dp[i] = (dp[i] + dp[i-2]) % mod
        if i < N:
            dp[i] = (dp[i] + B[i-1]) % mod
    return dp[N]

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(N, A, B))

