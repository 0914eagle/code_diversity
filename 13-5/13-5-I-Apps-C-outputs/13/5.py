
import sys

def hopscotch(N, X, Y):
    mod = 1000000007
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i >= X and j >= Y:
                dp[i][j] = (dp[i-X][j-Y] + dp[i-X][j]) % mod
            elif i >= X:
                dp[i][j] = dp[i-X][j] % mod
            elif j >= Y:
                dp[i][j] = dp[i][j-Y] % mod
    
    return dp[N][N]

if __name__ == "__main__":
    N, X, Y = map(int, sys.stdin.readline().strip().split())
    print(hopscotch(N, X, Y))

