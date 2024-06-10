
def get_min_coins(coins, value):
    # Initialize a dictionary to store the minimum number of coins needed for each value
    min_coins = {0: 0}
    for coin in coins:
        min_coins[coin] = 1

    # Loop through the values and calculate the minimum number of coins needed for each value
    for value in range(1, max(coins) * 2):
        if value not in min_coins:
            min_coins[value] = min(min_coins[value - coin] + 1 for coin in coins if value - coin >= 0)

    # Return the minimum number of coins needed for the given value
    return min_coins[value]

def main():
    # Read the number of coins and queries
    n, q = map(int, input().split())

    # Read the values of the coins
    coins = list(map(int, input().split()))

    # Read the queries
    queries = [int(input()) for _ in range(q)]

    # Solve the queries
    answers = [get_min_coins(coins, value) for value in queries]

    # Print the answers
    for answer in answers:
        print(answer)

if __name__ == '__main__':
    main()

