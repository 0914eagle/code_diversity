
def count_arrangements(n, m):
    MOD = 10**9 + 9
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = 1 if j % 2 == 0 else 0
            elif i == 1:
                dp[i][j] = 2 if j % 2 == 0 else 0
            else:
                dp[i][j] = (dp[i-1][j-2] + dp[i-1][j+2]) % MOD
    
    total_arrangements = sum(dp[-1]) % MOD
    return total_arrangements

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = count_arrangements(n, m)
    print(result)
