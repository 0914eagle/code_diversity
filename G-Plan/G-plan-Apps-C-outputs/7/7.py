
MOD = 10**9 + 7

def count_ways_to_paint_squares(N, M, conditions):
    dp = [[[0 for _ in range(4)] for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][0][3] = 1

    for i in range(1, N + 1):
        for j in range(M + 1):
            for k in range(4):
                dp[i][j][k] = dp[i - 1][j][k]
                if j > 0 and k != 3:
                    dp[i][j][k] += dp[i - 1][j - 1][3]
                dp[i][j][k] %= MOD

    for l, r, x in conditions:
        ans = 0
        for k in range(1, 4):
            ans += dp[r][x][k] - dp[l - 1][x][k]
            ans %= MOD
        print(ans)

if __name__ == "__main__":
    N, M = map(int, input().split())
    conditions = [list(map(int, input().split())) for _ in range(M)]
    count_ways_to_paint_squares(N, M, conditions)
