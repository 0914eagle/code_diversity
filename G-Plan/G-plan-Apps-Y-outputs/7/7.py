cost_to_obtain_set(n, k, s):
    if n < k:
        return -1
    
    dp = [[-1] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + i - s[i - 1])
    
    return dp[n][k]

if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input().strip()
    
    result = min_cost_to_obtain_set(n, k, s)
    print(result)
