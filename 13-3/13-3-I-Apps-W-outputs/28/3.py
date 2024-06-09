
def solve(n, m, a):
    # Initialize a dictionary to store the number of ways to get each card
    dp = {(1, 1): 1}
    
    # Iterate over the given cards
    for i in range(n):
        # Get the current card
        card = (1, a[i])
        
        # Iterate over the possible next cards
        for next_card in dp:
            # Get the current card's values
            x, y = card
            nx, ny = next_card
            
            # If the current card's values are even, the gray horse can paint a new card
            if x % 2 == 0 and y % 2 == 0:
                dp[(nx, ny)] += dp[card]
            
            # If the current card's values are not equal, the gray-and-white horse can paint a new card
            if x != y:
                dp[(x, ny)] += dp[card]
            
            # The white horse can paint a new card if the current card's values are even
            if x % 2 == 0 and y % 2 == 0:
                dp[(nx // 2, ny // 2)] += dp[card]
    
    # Return the number of ways to get the required cards
    return sum(dp.values())

