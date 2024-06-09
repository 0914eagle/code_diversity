
def solve(n, k, sequence, costs):
    # Initialize a dictionary to store the minimum cost to make the sequence unbalanced
    dp = {0: 0}
    
    # Loop through each position in the sequence
    for i in range(n):
        # If the current position is already unbalanced, skip it
        if dp[i] == float('inf'):
            continue
        
        # If the current position is balanced and the next position is also balanced, merge them into a single balanced sequence
        if sequence[i] == '(' and sequence[i+1] == ')':
            dp[i+2] = min(dp[i+2], dp[i] + costs[i])
        
        # If the current position is balanced and the next position is unbalanced, change the next position to balance the sequence
        if sequence[i] == '(' and sequence[i+1] == ')':
            dp[i+1] = min(dp[i+1], dp[i] + costs[i])
        
        # If the current position is unbalanced and the next position is balanced, change the current position to balance the sequence
        if sequence[i] == ')' and sequence[i+1] == '(':
            dp[i] = min(dp[i], dp[i+1] + costs[i+1])
    
    # If Bruce can always rebalance the sequence regardless of Barry's actions, return '?'
    if dp[n] != float('inf'):
        return '?'
    
    # Otherwise, return the minimum cost to make the sequence unbalanced
    return dp[n]

