
def longest_interesting_subsequence(A, S):
    # Initialize variables
    N = len(A)
    dp = [0] * (N + 1)
    
    # Loop through each element in the array
    for i in range(1, N + 1):
        # If the current element is less than or equal to S, we can include it in the subsequence
        if A[i - 1] <= S:
            dp[i] = max(dp[i - 1] + 1, dp[i])
        
        # If the current element is greater than S, we cannot include it in the subsequence
        else:
            dp[i] = dp[i - 1]
    
    # Return the length of the longest interesting subsequence
    return dp[N]

