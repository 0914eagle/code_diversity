
def f1(d, g, n, k):
    # Initialize variables
    max_coins = 0
    coins_left = d
    gladstone_coins_left = g
    distracted_rounds = k

    # Play the game
    for i in range(n):
        # Determine if Gladstone will be distracted during this round
        if distracted_rounds > 0:
            distracted_rounds -= 1
            continue

        # Determine the amount of coins to bet
        bet = min(coins_left, gladstone_coins_left)

        # Update the amount of coins left
        coins_left -= bet
        gladstone_coins_left -= bet

        # Update the maximum amount of coins
        max_coins = max(max_coins, coins_left)

    return max_coins

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    d, g, n, k = map(int, input().split())
    print(f1(d, g, n, k))

