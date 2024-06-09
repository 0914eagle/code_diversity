
def get_max_coins(price, coins):
    # Initialize a dictionary to store the number of coins for each denomination
    coins_dict = {1: 0, 5: 0, 10: 0, 25: 0}

    # Add the number of coins for each denomination to the dictionary
    for coin in coins:
        coins_dict[coin] += 1

    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0

    # Iterate through the dictionary and check if the number of coins for each denomination is greater than or equal to the price
    for denomination in coins_dict:
        if coins_dict[denomination] >= price:
            max_coins += price
            break
        else:
            max_coins += coins_dict[denomination]
            price -= coins_dict[denomination]

    # If the price is not zero, it is not possible to pay the exact amount without getting change back
    if price != 0:
        return "Impossible"

    return max_coins

