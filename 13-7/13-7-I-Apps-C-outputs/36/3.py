
def solve(price, num_coins):
    # Initialize a dictionary to store the number of coins for each value
    coins = {1: 0, 5: 0, 10: 0, 25: 0}

    # Add the number of coins for each value
    for value, count in num_coins.items():
        coins[value] += count

    # Initialize the maximum number of coins that can be used
    max_coins = 0

    # Loop through the values of coins and see if they can be used to pay the price
    for value in sorted(coins.keys(), reverse=True):
        # If the price is already paid, break the loop
        if price == 0:
            break
        # If the number of coins for the current value is greater than the price, use all the coins and break the loop
        if coins[value] >= price:
            max_coins += price
            break
        # If the number of coins for the current value is less than the price, use all the coins and continue the loop
        else:
            max_coins += coins[value]
            price -= coins[value]

    # If the price is not paid, return "Impossible"
    if price != 0:
        return "Impossible"

    # Return the maximum number of coins that can be used
    return max_coins

