
def get_coins(price, coins):
    # Initialize a dictionary to store the number of coins for each value
    coins_dict = {1: 0, 5: 0, 10: 0, 25: 0}

    # Loop through the coins and add them to the dictionary
    for coin in coins:
        coins_dict[coin] += 1

    # Initialize a variable to store the total number of coins
    total_coins = 0

    # Loop through the coins and add them to the total
    for coin, count in coins_dict.items():
        total_coins += count

    # Check if the total number of coins is greater than the price
    if total_coins < price:
        return "Impossible"

    # Initialize a variable to store the maximum number of coins that can be used
    max_coins = 0

    # Loop through the coins and find the maximum number of coins that can be used
    for coin, count in coins_dict.items():
        if count > 0:
            max_coins += 1
            price -= coin
            coins_dict[coin] -= 1

    return max_coins

def main():
    price, num_coins = map(int, input().split())
    coins = list(map(int, input().split()))
    result = get_coins(price, coins)
    print(result)

if __name__ == '__main__':
    main()

