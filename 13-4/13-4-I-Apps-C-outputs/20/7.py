
def solve(price, coins):
    # Initialize a dictionary to store the number of coins for each value
    coins_dict = {1: coins[0], 5: coins[1], 10: coins[2], 25: coins[3]}
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    # Loop through the dictionary and check if the current value is less than or equal to the price
    for value in coins_dict.keys():
        if value <= price:
            # If the current value is less than or equal to the price, calculate the number of coins that can be used for this value
            num_coins = price // value
            # Update the maximum number of coins if the current number of coins is greater than the previous maximum
            if num_coins > max_coins:
                max_coins = num_coins
            # Update the price by subtracting the current value multiplied by the number of coins that can be used
            price -= value * num_coins
    
    # If the price is not zero, it is not possible to pay the exact amount without getting change back
    if price != 0:
        return "Impossible"
    else:
        return max_coins

