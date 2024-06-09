
def solve(price, coins):
    # Initialize a dictionary to store the number of coins for each value
    coin_count = {1: 0, 5: 0, 10: 0, 25: 0}
    for coin in coins:
        coin_count[coin] += 1
    
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    
    # Iterate through the dictionary and check if the number of coins for each value is greater than the maximum number of coins that can be used
    for value, count in coin_count.items():
        if count > max_coins:
            max_coins = count
    
    # Check if the maximum number of coins that can be used is enough to pay the price
    if max_coins * value >= price:
        return max_coins
    else:
        return "Impossible"

