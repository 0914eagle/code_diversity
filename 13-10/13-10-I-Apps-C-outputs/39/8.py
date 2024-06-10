
def get_maximum_coins(price, coins):
    # Initialize a dictionary to store the number of coins for each coin value
    coin_counts = {1: 0, 5: 0, 10: 0, 25: 0}
    
    # Add the number of coins for each coin value to the dictionary
    for coin in coins:
        coin_counts[coin] += 1
    
    # Initialize a variable to store the total number of coins
    total_coins = 0
    
    # Loop through the coin values in descending order
    for coin_value in sorted(coin_counts.keys(), reverse=True):
        # If the coin value is less than or equal to the price, add the number of coins for that value to the total number of coins
        if coin_value <= price:
            total_coins += coin_counts[coin_value]
            # Subtract the coin value from the price
            price -= coin_value
    
    # If the price is not zero, it is not possible to pay the exact price without getting change back
    if price != 0:
        return "Impossible"
    
    # Return the total number of coins
    return total_coins

def main():
    # Read the price and the number of coins from stdin
    price = int(input())
    coins = list(map(int, input().split()))
    
    # Call the get_maximum_coins function and print the result
    print(get_maximum_coins(price, coins))

if __name__ == '__main__':
    main()

