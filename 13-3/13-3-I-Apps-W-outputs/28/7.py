
def solve(n, m, a):
    # Initialize a dictionary to store the number of ways to get each card
    dp = {(1, 1): 1}
    
    # Iterate through the given cards
    for i in range(n):
        # Get the current card
        card = (1, a[i])
        
        # Iterate through the previous cards
        for j in range(i):
            # Get the previous card
            prev_card = (1, a[j])
            
            # Check if the previous card is valid
            if prev_card in dp:
                # Get the number of ways to get the previous card
                num_ways = dp[prev_card]
                
                # Update the number of ways to get the current card
                dp[card] = (dp[card] if card in dp else 0) + num_ways
    
    # Return the number of ways to get the required cards
    return dp[(1, m)]

