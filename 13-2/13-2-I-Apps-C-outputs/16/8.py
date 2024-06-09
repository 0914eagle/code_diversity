
def solve(n, k, seq, costs):
    # Initialize a dictionary to store the minimum effort required to make the string impossible to balance
    dp = {0: 0}
    
    # Loop through each position in the string
    for i in range(n):
        # If the current position is already impossible to balance, skip it
        if dp[i] == float('inf'):
            continue
        
        # If the current position is balanced and Bruce can still balance it with k moves left, update the minimum effort required to make it impossible
        if seq[i] == '(' and k > 0:
            dp[i+1] = min(dp[i+1], dp[i] + costs[i])
        
        # If the current position is unbalanced and Bruce can still balance it with k moves left, update the minimum effort required to make it impossible
        if seq[i] == ')' and k > 0:
            dp[i+1] = min(dp[i+1], dp[i] + costs[i])
        
        # If the current position is impossible to balance, set the minimum effort required to make it impossible to float('inf')
        if dp[i+1] == float('inf'):
            dp[i+1] = float('inf')
    
    # Return the minimum effort required to make the string impossible to balance
    return dp[n]

