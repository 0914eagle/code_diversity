
MOD = 10**9 + 7

def count_ways_to_paint_squares(N, M, conditions):
    dp = [[[0] * 4 for _ in range(N + 1)] for _ in range(M + 1)
    dp[0][0][0] = 1

    for i in range(1, M + 1):
        l, r, x = conditions[i - 1]
        for j in range(l, r + 1):
            for k in range(1, 4):
                dp[i][j][k] = dp[i - 1][j][k]
        for j in range(l, r + 1):
            for k in range(1, 4):
                if k != x:
                    dp[i][j][k] += dp[i][j - 1][k - 1]
                    dp[i][j][k] %= MOD

    total_ways = 0
    for k in range(1, 4):
        total_ways += dp[M][N][k]
        total_ways %= MOD

    return total_ways

if __name__ == "__main__":
    N, M = map(int, input().split())
    conditions = [list(map(int, input().split())) for _ in range(M)]
    result = count_ways_to_paint_squares(N, M, conditions)
    print(result)
