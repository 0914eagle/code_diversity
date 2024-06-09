
def get_max_profit(n, m, l, s, c):
    # Initialize a two-dimensional table to store the maximum profit for each candidate and aggressiveness level
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Loop through each candidate and aggressiveness level
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the candidate is not recruited, the maximum profit is 0
            if i == 0:
                dp[i][j] = 0
            # If the candidate is recruited and has aggressiveness level j, the maximum profit is the profit from recruiting the candidate plus the profit from the events on stage
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + s[i - 1] + c[j])

    # Return the maximum profit for the last candidate and aggressiveness level
    return dp[n][m]

