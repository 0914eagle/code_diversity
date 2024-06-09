
def get_max_happiness(n, m, a, b):
    # Initialize the dp table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the base case
    for i in range(m):
        dp[i][0] = a[i]

    # Fill in the dp table
    for i in range(m):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] + b[i - 1])

    return dp[m - 1][n]

