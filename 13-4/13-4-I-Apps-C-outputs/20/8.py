
def get_max_coins(price, coins):
    # Initialize a dictionary to store the number of coins for each denomination
    coin_dict = {1: 0, 5: 0, 10: 0, 25: 0}
    for coin in coins:
        coin_dict[coin] += 1
    
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    
    # Iterate through the dictionary and calculate the maximum number of coins that can be used for each denomination
    for coin, count in coin_dict.items():
        max_coins += count // price * coin
    
    # If the maximum number of coins is less than the price, return "Impossible"
    if max_coins < price:
        return "Impossible"
    
    # Otherwise, return the maximum number of coins that can be used
    return max_coins

