
def get_coins(price, coins):
    # Initialize a dictionary to store the number of coins for each value
    coins_dict = {1: 0, 5: 0, 10: 0, 25: 0}
    
    # Add the number of coins for each value to the dictionary
    for coin in coins:
        coins_dict[coin] += 1
    
    # Initialize a variable to store the total value of the coins
    total_value = 0
    
    # Loop through the dictionary and add the value of each coin to the total value
    for value, count in coins_dict.items():
        total_value += value * count
    
    # If the total value is less than the price, return -1
    if total_value < price:
        return -1
    
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    
    # Loop through the dictionary and find the maximum number of coins that can be used for the price
    for value, count in coins_dict.items():
        if price // value == 0:
            continue
        max_coins = max(max_coins, count)
        price -= value * max_coins
    
    return max_coins

def main():
    price = int(input())
    coins = list(map(int, input().split()))
    result = get_coins(price, coins)
    if result == -1:
        print("Impossible")
    else:
        print(result)

if __name__ == '__main__':
    main()

