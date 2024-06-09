
def count_ways_to_paint(N, M, c):
    mod = 100003
    
    dp = [[0] * (M+1) for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        for j in range(M+1):
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod
            if j > c[i-1]:
                dp[i][j] = (dp[i][j] + dp[i][j-1] - dp[i-1][j-c[i-1]-1]) % mod
            else:
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % mod
    
    X = dp[N][M]
    Y = X % mod
    
    return X, Y

# Input
N, M = map(int, input().split())
c = list(map(int, input().split()))

# Output
X, Y = count_ways_to_paint(N, M, c)
print(X, Y)
