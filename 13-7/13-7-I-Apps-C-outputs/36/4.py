
def solve(price, num_coins):
    # Initialize a dictionary to store the number of coins for each denomination
    coins = {1: 0, 5: 0, 10: 0, 25: 0}
    
    # Add the number of coins for each denomination to the dictionary
    for i in range(len(num_coins)):
        coins[i+1] = num_coins[i]
    
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    
    # Iterate through the dictionary and check if the number of coins for each denomination is greater than or equal to the price
    for denomination in coins:
        if coins[denomination] >= price:
            max_coins += 1
            price -= denomination
    
    # If the price is not zero, it is not possible to pay the exact amount without getting change back
    if price != 0:
        return "Impossible"
    
    # Return the maximum number of coins that can be used to pay the price
    return max_coins

