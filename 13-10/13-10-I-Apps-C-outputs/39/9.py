
def get_maximum_coins(price, coins):
    # Initialize a dictionary to store the number of coins for each denomination
    coin_dict = {1: 0, 5: 0, 10: 0, 25: 0}
    
    # Loop through the coins and add them to the dictionary
    for coin in coins:
        coin_dict[coin] += 1
    
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    
    # Loop through the coins and check if they can be used to pay the price
    for coin in coins:
        # If the coin is equal to the price, return the maximum number of coins
        if coin == price:
            return coin_dict[coin]
        # If the coin is greater than the price, subtract the price from the coin and add the difference to the maximum number of coins
        elif coin > price:
            max_coins += price // coin
            price -= price // coin * coin
    
    # If no coin is equal to the price, return the maximum number of coins
    return max_coins

def main():
    price = int(input())
    coins = list(map(int, input().split()))
    print(get_maximum_coins(price, coins))

if __name__ == '__main__':
    main()

