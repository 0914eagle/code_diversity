
def get_min_cost(positions, k):
    n = len(positions)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = float('inf')
                for v in range(positions[i - 1], positions[j - 1] + 1):
                    dp[i][j] = min(dp[i][j], dp[i][v] + dp[v][j] + abs(positions[i - 1] - v) ** k + abs(positions[j - 1] - v) ** k)
    return dp[1][n]

