
def solve(n, k, seq, costs):
    # Initialize a dictionary to store the minimum cost to make the string impossible to balance
    dp = {0: 0}
    
    # Loop through each position in the string
    for i in range(n):
        # If the current position is already impossible to balance, skip it
        if dp[i] == float('inf'):
            continue
        
        # If the current position is balanced and the next position is not balanced, add the cost of changing the current position to the minimum cost
        if seq[i] == '(' and seq[i+1] == ')':
            dp[i+1] = min(dp[i+1], dp[i] + costs[i])
        
        # If the current position is not balanced and the next position is balanced, add the cost of changing the current position to the minimum cost
        if seq[i] == ')' and seq[i+1] == '(':
            dp[i+1] = min(dp[i+1], dp[i] + costs[i])
    
    # If the last position is impossible to balance, return the minimum cost, otherwise return infinity
    if dp[n] == float('inf'):
        return '?'
    else:
        return dp[n]

