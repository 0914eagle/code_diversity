
def get_maximum_coins(price, coins):
    # Initialize a dictionary to store the number of coins for each denomination
    denomination_coins = {1: 0, 5: 0, 10: 0, 25: 0}
    
    # Add the number of coins for each denomination to the dictionary
    for coin in coins:
        denomination_coins[coin] += 1
    
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    
    # Iterate through the dictionary and find the maximum number of coins that can be used
    for denomination, num_coins in denomination_coins.items():
        if denomination * num_coins <= price:
            max_coins += num_coins
            price -= denomination * num_coins
    
    # If the price is not zero, it is not possible to pay the exact amount without getting change back
    if price != 0:
        return "Impossible"
    
    return max_coins

