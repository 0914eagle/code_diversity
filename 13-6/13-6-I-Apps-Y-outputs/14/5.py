
def get_maximum_sum(a, k, x):
    n = len(a)
    if k > n or x > n or x < k:
        return -1
    
    # Initialize dp table with -1
    dp = [-1] * (n + 1)
    dp[0] = 0
    
    # Loop through all possible ranges
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if i - j < k:
                break
            if dp[j] != -1 and dp[i] < dp[j] + a[i - 1]:
                dp[i] = dp[j] + a[i - 1]
    
    # Return the maximum sum
    return dp[n]

