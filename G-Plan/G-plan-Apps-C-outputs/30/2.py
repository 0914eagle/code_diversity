
def count_valid_arrangements(n, m):
    MOD = 10**9 + 9
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = 4 if j % 2 == 0 else 2
            elif i == 1:
                dp[i][j] = 2 * dp[i - 1][j] % MOD
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i - 2][j]) % MOD
    
    return dp[n - 1][m - 1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = count_valid_arrangements(n, m)
    print(result)
