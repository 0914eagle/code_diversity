
def solve(P, N_1, N_5, N_10, N_25):
    # Initialize a dictionary to store the number of coins for each denomination
    coins = {
        1: N_1,
        5: N_5,
        10: N_10,
        25: N_25,
    }
    
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    
    # Iterate through the dictionary of coins and find the maximum number of coins that can be used
    for denomination, count in coins.items():
        # Check if the number of coins for the current denomination is greater than the number of coins needed for the price
        if count >= P // denomination:
            # Add the number of coins needed for the price to the maximum number of coins
            max_coins += P // denomination
            # Subtract the number of coins needed for the price from the current number of coins
            coins[denomination] -= P // denomination
            # Break out of the loop since we have found the maximum number of coins that can be used
            break
    
    # Check if the maximum number of coins is greater than the number of coins needed for the price
    if max_coins < P:
        # Return "Impossible" since it is not possible to use the maximum number of coins to pay the price without getting any change back
        return "Impossible"
    else:
        # Return the maximum number of coins that can be used to pay the price
        return max_coins

