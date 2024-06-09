
def max_cost(s, p):
    n = len(s)
    if n == 0 or p == 0:
        return 0

    # Convert the string to a list of characters
    chars = list(s)

    # Initialize the dp table with 0's
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Populate the table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if chars[i - 1] == chars[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

    # Return the maximum cost
    return dp[n][n]

