
def get_max_profit(n, h, m, restrictions):
    # Initialize the dp table with 0 as the base case
    dp = [0] * (n + 1)

    # Loop through each restriction
    for l, r, x in restrictions:
        # Loop through each spot
        for i in range(l, r + 1):
            # Update the dp table with the maximum of the current height and the previous height plus the profit from the current spot
            dp[i] = max(dp[i], dp[i - 1] + (i - l + 1) ** 2)

            # If the current height is greater than the maximum allowed height, break the loop
            if dp[i] > x:
                break

    # Return the maximum profit possible
    return dp[n]

