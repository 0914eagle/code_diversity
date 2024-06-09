
def get_max_profit(n, m, l, s, c):
    # Initialize the dp table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Loop through each candidate
    for i in range(1, n + 1):
        # Loop through each aggressiveness level
        for j in range(1, m + 1):
            # If the candidate is already accepted, skip
            if dp[i - 1][j] != 0:
                continue
            # If the candidate is not accepted and the aggressiveness level is higher than the current level, skip
            if l[i - 1] > j:
                continue
            # If the candidate is not accepted and the aggressiveness level is lower than the current level, skip
            if l[i - 1] < j:
                continue
            # If the candidate is not accepted and the aggressiveness level is equal to the current level, check if it's more profitable to accept the candidate
            if dp[i - 1][j] < dp[i - 1][j - 1] + c[l[i - 1]] - s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + c[l[i - 1]] - s[i - 1]
            else:
                dp[i][j] = dp[i - 1][j]

    # Return the maximum profit
    return max(dp[n])

