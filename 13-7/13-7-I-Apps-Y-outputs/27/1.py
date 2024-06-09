
def get_max_beauty(n, k, x, a):
    if k > n or x > n or x < k:
        return -1
    
    # Initialize the dp table with -1
    dp = [-1] * (n + 1)
    dp[0] = 0
    
    # Loop through each position in the array
    for i in range(1, n + 1):
        # If the current position is within the repost limit
        if i <= x:
            # Update the dp table with the maximum value of the current position and the previous positions
            dp[i] = max(dp[i - 1], dp[i - k] + a[i - 1])
        else:
            # If the current position is not within the repost limit, just copy the value from the previous position
            dp[i] = dp[i - 1]
    
    # Return the maximum value in the dp table
    return dp[n]

