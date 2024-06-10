
def get_change(price, coins):
    # Initialize a dictionary to store the number of coins for each denomination
    coins_dict = {1: 0, 5: 0, 10: 0, 25: 0}
    
    # Add the number of coins for each denomination to the dictionary
    for coin in coins:
        coins_dict[coin] += 1
    
    # Initialize a variable to store the total number of coins
    total_coins = 0
    
    # Iterate through the dictionary and add the number of coins for each denomination to the total
    for coin, count in coins_dict.items():
        total_coins += count
    
    # If the total number of coins is less than the price, return "Impossible"
    if total_coins < price:
        return "Impossible"
    
    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0
    
    # Iterate through the dictionary and find the maximum number of coins that can be used for each denomination
    for coin, count in coins_dict.items():
        max_coins += count // price * coin
    
    # Return the maximum number of coins that can be used
    return max_coins

def main():
    price = int(input())
    coins = list(map(int, input().split()))
    print(get_change(price, coins))

if __name__ == '__main__':
    main()

