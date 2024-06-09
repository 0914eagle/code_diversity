
def solve(price, num_coins):
    # Initialize a dictionary to store the number of coins for each value
    coins = {1: 0, 5: 0, 10: 0, 25: 0}

    # Add the number of coins for each value
    for value, count in num_coins.items():
        coins[value] += count

    # Initialize the maximum number of coins that can be used
    max_coins = 0

    # Loop through the values of coins and check if they can be used to pay the price
    for value in sorted(coins.keys(), reverse=True):
        # If the value is greater than the price, continue to the next value
        if value > price:
            continue

        # If the value is equal to the price, add the number of coins for that value to the maximum number of coins
        if value == price:
            max_coins += coins[value]
            break

        # If the value is less than the price, add the number of coins for that value to the maximum number of coins and subtract the value from the price
        max_coins += coins[value]
        price -= value

    # If the maximum number of coins is 0, it means that it's impossible to pay the price without getting any change back
    if max_coins == 0:
        return "Impossible"

    # Return the maximum number of coins that can be used to pay the price
    return max_coins

