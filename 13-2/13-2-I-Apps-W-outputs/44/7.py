
def get_sorted_probability(a, k):
    n = len(a)
    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            for x in range(i-1, -1, -1):
                if a[x] == 0:
                    dp[i][j] = (dp[i][j] + dp[x][j-1]) % 1000000007
                else:
                    dp[i][j] = (dp[i][j] + dp[x][j]) % 1000000007
    return dp[n][k]

