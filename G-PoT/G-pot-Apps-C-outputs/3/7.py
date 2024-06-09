
MOD = 100003

def count_ways(N, M, c):
    dp = [[0] * (M+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(M+1):
            for k in range(j, M+1):
                dp[i][k] = (dp[i][k] + dp[i-1][j]) % MOD

    total_ways = sum(dp[N])
    X = total_ways // MOD
    Y = total_ways % MOD

    return X, Y

# Input
N, M = map(int, input().split())
c = list(map(int, input().split()))

# Output
X, Y = count_ways(N, M, c)
print(X, Y)
