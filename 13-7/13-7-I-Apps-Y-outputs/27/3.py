
def get_max_sum(a, k, x):
    n = len(a)
    if k > x or k > n:
        return -1
    
    # Initialize the dp table with -1
    dp = [-1] * (n + 1)
    dp[0] = 0
    
    # Loop through each position in the array
    for i in range(1, n + 1):
        # If we can repost the current picture
        if i <= x:
            # Update the maximum sum by including the current picture
            dp[i] = max(dp[i - 1], dp[i - k] + a[i - 1])
        else:
            # If we can't repost the current picture, just copy the previous value
            dp[i] = dp[i - 1]
    
    return dp[n]

