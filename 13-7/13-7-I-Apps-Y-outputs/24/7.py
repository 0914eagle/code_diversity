
def get_min_coins(values, total):
    # Initialize a list to store the minimum number of coins required for each total
    min_coins = [0] * (total + 1)
    # Base case: min_coins[0] = 0
    for i in range(1, total + 1):
        # Initialize the minimum number of coins required for current total to infinity
        min_coins[i] = float('inf')
        # Loop through all values of coins
        for value in values:
            # Check if the current total is a multiple of the current value of coin
            if i % value == 0:
                # Calculate the minimum number of coins required for current total
                min_coins[i] = min(min_coins[i], min_coins[i - value] + 1)
    return min_coins[-1]

def get_coins(values, total):
    # Initialize a list to store the coins used for each total
    coins = [[]] * (total + 1)
    # Base case: coins[0] = []
    for i in range(1, total + 1):
        # Initialize the coins used for current total to None
        coins[i] = None
        # Loop through all values of coins
        for value in values:
            # Check if the current total is a multiple of the current value of coin
            if i % value == 0:
                # Calculate the coins used for current total
                coins[i] = coins[i - value] + [value]
                break
    return coins[-1]

def main():
    n, q = map(int, input().split())
    values = list(map(int, input().split()))
    for _ in range(q):
        total = int(input())
        print(get_min_coins(values, total))

if __name__ == '__main__':
    main()

