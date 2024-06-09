
import sys

def solve():
    H, N = map(int, input().split())
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        A[i], B[i] = map(int, input().split())
    
    # DP approach
    dp = [0] * (H + 1)
    dp[0] = 0
    for i in range(1, H + 1):
        for j in range(1, N + 1):
            if i - A[j] >= 0:
                dp[i] = min(dp[i], dp[i - A[j]] + B[j])
    
    return dp[H]

print(solve())

