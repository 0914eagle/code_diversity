
def get_max_happiness(n, m, a, b):
    # Initialize the dp table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if j < a[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + b[i - 1])

    # Return the maximum total happiness
    return dp[m][n]

