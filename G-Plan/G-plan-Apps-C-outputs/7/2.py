
MOD = 10**9 + 7

def count_ways_to_paint_squares(N, M, conditions):
    dp = [[[0 for _ in range(4)] for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    for i in range(1, N + 1):
        for j in range(M + 1):
            for k in range(4):
                dp[i][j][k] = dp[i - 1][j][k]
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            l, r, x = conditions[j - 1]
            for k in range(1, 4):
                if l <= i <= r:
                    if x == 1 and k == 1:
                        dp[i][j][k] = 0
                    elif x == 1 and k != 1:
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1]
                    elif x == 2:
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1] + dp[i - 1][j - 1][k + 1]
                    elif x == 3:
                        dp[i][j][k] = dp[i - 1][j - 1][k]
    
    total_ways = sum(dp[N][M]) % MOD
    return total_ways

if __name__ == "__main__":
    N, M = map(int, input().split())
    conditions = [list(map(int, input().split())) for _ in range(M)]
    result = count_ways_to_paint_squares(N, M, conditions)
    print(result)
