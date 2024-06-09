
def longest_interesting_subsequence(A, S):
    # Initialize variables
    N = len(A)
    dp = [0] * (N + 1)
    
    # Loop through each element in the array
    for i in range(1, N + 1):
        # If the sum of the first K elements is less than or equal to S, update the length of the longest interesting subsequence
        if sum(A[:i]) <= S:
            dp[i] = max(dp[i - 1], i)
        # If the sum of the last K elements is less than or equal to S, update the length of the longest interesting subsequence
        if sum(A[i:]) <= S:
            dp[i] = max(dp[i], dp[i - 1])
    
    # Return the length of the longest interesting subsequence
    return dp[N]

