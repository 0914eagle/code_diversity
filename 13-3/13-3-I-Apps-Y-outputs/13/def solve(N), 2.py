
import sys

def solve(N):
    mod = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(10):
            if j == 0 or j == 9:
                dp[i] += dp[i - 1]
            else:
                dp[i] += dp[i - 1] * 8
        dp[i] %= mod
    return dp[N]

if __name__ == '__main__':
    N = int(sys.stdin.read())
    print(solve(N))

