
def count_valid_arrangements(n, m):
    MOD = 10**9 + 9
    dp = [[0] * m for _ in range(n)]
    
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i > 0:
                dp[i][j] += dp[i - 1][(j - 2) % m] + dp[i - 1][(j + 2) % m]
            if i > 1:
                dp[i][j] += dp[i - 2][(j - 1) % m] + dp[i - 2][(j + 1) % m]
            dp[i][j] %= MOD
    
    return dp[n - 1][m - 1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = count_valid_arrangements(n, m)
    print(result)
