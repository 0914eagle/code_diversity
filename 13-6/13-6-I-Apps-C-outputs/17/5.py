
def get_max_coins(d, g, n, k):
    # Initialize the maximum number of coins as 0
    max_coins = 0
    
    # Loop through each round
    for i in range(n):
        # If Gladstone is distracted during this round
        if i in k:
            # Donald can look at Gladstone's cards and swap them
            # to increase his chances of winning
            max_coins += d
        else:
            # Donald needs to choose his bet carefully to avoid losing
            max_coins += min(d, g)
    
    # Return the maximum number of coins Donald can be certain to have
    return max_coins

