
def get_min_pockets(coins):
    # Sort the coins in non-decreasing order
    coins.sort()
    # Initialize the number of pockets as 1
    num_pockets = 1
    # Iterate through the coins
    for i in range(1, len(coins)):
        # If the current coin is different from the previous coin, increase the number of pockets
        if coins[i] != coins[i-1]:
            num_pockets += 1
    return num_pockets

def main():
    n = int(input())
    coins = list(map(int, input().split()))
    print(get_min_pockets(coins))

if __name__ == '__main__':
    main()

