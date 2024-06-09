
def get_max_beauty(a, k, x):
    n = len(a)
    if k > x or k > n:
        return -1
    
    # Initialize dp table with -1
    dp = [-1] * (n + 1)
    dp[0] = 0
    
    # Loop through each position in the array
    for i in range(1, n + 1):
        # If the current position is within the range of reposted pictures
        if i <= x:
            # Calculate the maximum beauty by including the current picture
            dp[i] = max(dp[i - 1], dp[i - k] + a[i - 1])
        else:
            # If the current position is not within the range of reposted pictures,
            # copy the value from the previous position
            dp[i] = dp[i - 1]
    
    return dp[n]

