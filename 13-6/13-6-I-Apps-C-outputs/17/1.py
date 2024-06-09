
def get_maximum_coins(d, g, n, k):
    # Initialize variables
    maximum_coins = 0
    current_coins = d
    gladstone_coins = g
    rounds_played = 0
    
    # Loop through each round
    while rounds_played < n:
        # If Gladstone is distracted, look at his cards and swap them if necessary
        if rounds_played in range(k):
            # Swap cards if necessary
            if current_coins > gladstone_coins:
                current_coins += gladstone_coins
                gladstone_coins = current_coins - gladstone_coins
                current_coins -= gladstone_coins
        
        # Both players place their bets
        current_coins -= 1
        gladstone_coins -= 1
        
        # Update the maximum coins
        maximum_coins = max(maximum_coins, current_coins)
        
        # Update the number of rounds played
        rounds_played += 1
    
    # Return the maximum coins
    return maximum_coins

