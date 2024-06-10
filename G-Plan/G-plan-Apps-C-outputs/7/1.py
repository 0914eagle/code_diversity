
MOD = 10**9 + 7

def count_ways_to_paint_squares(N, M, conditions):
    dp = [[[0 for _ in range(4)] for _ in range(N + 1)] for _ in range(M + 1)
    dp[0][0][3] = 1

    for i in range(1, M + 1):
        l, r, x = conditions[i - 1]
        for j in range(N + 1):
            for k in range(4):
                if k == 3:
                    dp[i][j][3] = (dp[i][j][3] + dp[i - 1][j][3]) % MOD
                elif l <= j <= r:
                    dp[i][j][k] = dp[i - 1][j][k] * (k == x) % MOD
                else:
                    dp[i][j][k] = dp[i - 1][j][k] * (k != x) % MOD

    total_ways = sum(dp[M][N]) % MOD
    return total_ways

if __name__ == "__main__":
    N, M = map(int, input().split())
    conditions = [list(map(int, input().split())) for _ in range(M)]
    result = count_ways_to_paint_squares(N, M, conditions)
    print(result)
