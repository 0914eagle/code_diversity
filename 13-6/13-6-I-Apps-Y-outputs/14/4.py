
def get_max_beauty(a, k, x):
    n = len(a)
    if k > x or k > n:
        return -1
    
    # Initialize dp table with all -1
    dp = [-1] * (n + 1)
    dp[0] = 0
    
    # Populate the dp table
    for i in range(1, n + 1):
        for j in range(i - k, i):
            if dp[j] != -1:
                dp[i] = max(dp[i], dp[j] + a[i - 1])
    
    return dp[n]

