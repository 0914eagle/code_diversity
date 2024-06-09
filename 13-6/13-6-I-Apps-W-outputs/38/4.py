
def get_maximum_happiness(n, m, a, b):
    # Initialize the dp table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1:
                dp[i][j] = max(a[i - 1] + dp[i][j - 1], dp[i - 1][j])
            else:
                dp[i][j] = max(a[i - 1] + dp[i][j - 1], b[i - 1] + dp[i - 1][j - 1], dp[i - 1][j])

    # Return the maximum happiness
    return dp[m][n]

