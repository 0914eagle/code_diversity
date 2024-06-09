
import sys

def solve(N):
    mod = 10**9 + 7
    dp = [[0] * 10 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
    return dp[N][9]

if __name__ == "__main__":
    N = int(input())
    print(solve(N))

