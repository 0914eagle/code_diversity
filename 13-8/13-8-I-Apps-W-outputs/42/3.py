
import sys

def solve(r_1, c_1, r_2, c_2):
    mod = 1000000007
    dp = [[0] * (c_2+1) for _ in range(r_2+1)]
    dp[0][0] = 1
    for i in range(r_1, r_2+1):
        for j in range(c_1, c_2+1):
            if i == 0 and j == 0:
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
    return sum(dp[r_2]) % mod

if __name__ == '__main__':
    r_1, c_1, r_2, c_2 = map(int, sys.stdin.readline().split())
    print(solve(r_1, c_1, r_2, c_2))

