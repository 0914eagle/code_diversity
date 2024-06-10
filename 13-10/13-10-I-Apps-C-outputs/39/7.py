
def get_change(price, coins):
    # Initialize a dictionary to store the count of each coin
    coin_count = {}
    for coin in coins:
        coin_count[coin] = 0

    # Initialize the maximum number of coins that can be used
    max_coins = 0

    # Loop through the coins and calculate the maximum number of coins that can be used
    for coin in coins:
        # Calculate the number of coins that can be used for the current coin
        num_coins = price // coin
        # If the number of coins is greater than the current maximum, update the maximum
        if num_coins > max_coins:
            max_coins = num_coins
        # Add the number of coins to the dictionary
        coin_count[coin] += num_coins
        # Update the price after using the coins
        price -= num_coins * coin

    # If the price is not zero, it is not possible to pay the exact amount
    if price != 0:
        return "Impossible"
    else:
        # Return the maximum number of coins that can be used
        return max_coins

def main():
    # Read the input from stdin
    price = int(input())
    coins = list(map(int, input().split()))
    # Call the get_change function and print the result
    result = get_change(price, coins)
    print(result)

if __name__ == '__main__':
    main()

