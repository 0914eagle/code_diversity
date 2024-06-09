
import sys

def solve(r1, c1, r2, c2):
    mod = 10**9 + 7
    dp = [[0] * (c2+1) for _ in range(r2+1)]
    dp[0][0] = 1
    for i in range(1, r2+1):
        for j in range(1, c2+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
    return sum(dp[r2][c2:c1-1]) % mod

if __name__ == "__main__":
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    print(solve(r1, c1, r2, c2))

