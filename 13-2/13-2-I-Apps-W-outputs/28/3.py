
def get_max_profit(n, h, m, restrictions):
    # Initialize the dp table with 0 as the base case
    dp = [0] * (n + 1)

    # Loop through each restriction
    for l, r, x in restrictions:
        # Loop through each spot on the street
        for i in range(l, r + 1):
            # Check if the current spot is within the restriction
            if i >= l and i <= r:
                # Update the dp table with the maximum profit possible
                dp[i] = max(dp[i], dp[i - 1] + (x - h) ** 2)

    # Return the maximum profit possible
    return dp[n]

