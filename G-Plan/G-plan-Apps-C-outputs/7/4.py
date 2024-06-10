
MOD = 10**9 + 7

def count_ways_to_paint_squares(N, M, conditions):
    dp = [[[0 for _ in range(4)] for _ in range(N + 1)] for _ in range(M + 1)
    dp[0][0][0] = 1

    for i in range(1, M + 1):
        l, r, x = conditions[i - 1]
        for j in range(1, N + 1):
            for k in range(1, 4):
                dp[i][j][k] = dp[i - 1][j][k]
            if l <= j <= r:
                for k in range(1, 4):
                    if k != x:
                        dp[i][j][x] += dp[i - 1][j - 1][k]
                        dp[i][j][x] %= MOD

    total_ways = sum(dp[M][N][1:]) % MOD
    return total_ways

if __name__ == "__main__":
    N, M = map(int, input().split())
    conditions = [list(map(int, input().split())) for _ in range(M)]
    
    result = count_ways_to_paint_squares(N, M, conditions)
    print(result)
