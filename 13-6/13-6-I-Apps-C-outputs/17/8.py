
def get_max_coins(d, g, n, k):
    # Initialize variables
    max_coins = 0
    distracted_rounds = 0
    
    # Play the game
    for i in range(n):
        # Determine if Gladstone is distracted
        if distracted_rounds < k:
            # Gladstone is distracted, Donald can look at his cards and swap them
            # to increase his chances of winning
            distracted_rounds += 1
        else:
            # Gladstone is not distracted, Donald must choose his bet carefully
            # to avoid losing coins
            pass
        
        # Update the maximum coins
        max_coins = max(max_coins, d, g)
    
    # Return the maximum coins
    return max_coins

