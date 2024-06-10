
def find_max_coins(price, coins):
    # Initialize a dictionary to store the maximum number of coins for each value
    max_coins = {0: 0}
    
    # Loop through the coins and calculate the maximum number of coins for each value
    for coin in coins:
        for i in range(coin, price + 1):
            max_coins[i] = max(max_coins[i], max_coins[i - coin] + 1)
    
    # Return the maximum number of coins for the given price
    return max_coins[price]

def main():
    price = int(input())
    coins = list(map(int, input().split()))
    print(find_max_coins(price, coins))

if __name__ == '__main__':
    main()

