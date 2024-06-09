
def get_max_profit(n, m, l, s, c):
    # Initialize the dp table with 0 as the base case
    dp = [0] * (n + 1)

    # Loop through each candidate
    for i in range(1, n + 1):
        # Loop through each aggressiveness level
        for j in range(1, m + 1):
            # Check if the current candidate is recruited
            if l[i - 1] == j:
                # If the current candidate is recruited, calculate the profit
                dp[i] = max(dp[i], dp[i - 1] + c[j - 1] - s[i - 1])
            # If the current candidate is not recruited, calculate the profit
            else:
                dp[i] = max(dp[i], dp[i - 1])

    # Return the maximum profit
    return dp[n]

