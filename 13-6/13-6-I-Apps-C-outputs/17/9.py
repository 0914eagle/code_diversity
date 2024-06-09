
def get_max_coins(d, g, n, k):
    # Initialize variables
    max_coins = 0
    distracted_rounds = 0
    
    # Loop through each round
    for i in range(n):
        # If Gladstone is distracted, Donald can look at his cards and swap them to win the round
        if distracted_rounds < k:
            distracted_rounds += 1
            continue
        
        # Otherwise, Donald chooses the minimum of the two amounts of coins
        coins = min(d, g)
        
        # Update the amounts of coins
        d -= coins
        g -= coins
        
        # Update the maximum amount of coins
        max_coins = max(max_coins, d)
    
    return max_coins

