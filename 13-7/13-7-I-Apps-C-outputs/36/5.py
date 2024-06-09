
def solve(price, coins):
    # Initialize a dictionary to store the number of coins for each value
    coin_dict = {1: coins[0], 5: coins[1], 10: coins[2], 25: coins[3]}
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    # Loop through the dictionary and check if the number of coins for each value is greater than or equal to the price
    for value, num_coins in coin_dict.items():
        if num_coins >= price // value:
            max_coins += price // value
            price %= value
    # If the price is not zero, it is not possible to pay the exact amount without getting change back
    if price != 0:
        return "Impossible"
    return max_coins

