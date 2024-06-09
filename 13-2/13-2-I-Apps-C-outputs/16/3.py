
def solve(n, k, seq, costs):
    # Initialize a dictionary to store the minimum effort required to make the sequence unbalanced
    dp = {0: 0}
    
    # Loop through each position in the sequence
    for i in range(n):
        # If the current position is already unbalanced, skip it
        if dp[i] == float('inf'):
            continue
        
        # If the current position is balanced and the next position is also balanced, update the minimum effort required to make the sequence unbalanced
        if seq[i] == '(' and seq[i+1] == ')':
            dp[i+1] = min(dp[i+1], dp[i] + costs[i])
        
        # If the current position is balanced and the next position is unbalanced, update the minimum effort required to make the sequence unbalanced
        if seq[i] == '(' and seq[i+1] == '(':
            dp[i+1] = min(dp[i+1], dp[i] + costs[i])
        
        # If the current position is unbalanced and the next position is balanced, update the minimum effort required to make the sequence unbalanced
        if seq[i] == ')' and seq[i+1] == ')':
            dp[i+1] = min(dp[i+1], dp[i] + costs[i])
        
        # If the current position is unbalanced and the next position is unbalanced, update the minimum effort required to make the sequence unbalanced
        if seq[i] == ')' and seq[i+1] == '(':
            dp[i+1] = min(dp[i+1], dp[i] + costs[i])
    
    # If the last position is balanced, return the minimum effort required to make the sequence unbalanced
    if seq[n-1] == '(':
        return dp[n-1]
    
    # If the last position is unbalanced, return infinity
    return float('inf')

