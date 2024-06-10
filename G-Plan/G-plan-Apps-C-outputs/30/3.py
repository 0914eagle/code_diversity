
def count_arrangements(n, m):
    MOD = 10**9 + 9
    dp = [[0] * m for _ in range(n)]
    
    for j in range(m):
        dp[0][j] = 1
    
    for i in range(1, n):
        for j in range(m):
            dp[i][j] = (dp[i-1][(j-2)%m] + dp[i-1][(j+2)%m]) % MOD
    
    total_arrangements = sum(dp[-1]) % MOD
    return total_arrangements

if __name__ == '__main__':
    n, m = map(int, input().split())
    result = count_arrangements(n, m)
    print(result)
