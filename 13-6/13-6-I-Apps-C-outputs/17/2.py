
def f1(d, g, n, k):
    # Initialize variables
    max_coins = 0
    coins_left = d
    gladstone_coins_left = g
    distracted_rounds = k

    # Play the game
    for i in range(n):
        # If Gladstone is distracted, Donald can look at his cards and swap them
        if i in range(k):
            # Donald can swap his cards with Gladstone's cards
            pass
        else:
            # Donald can't swap his cards, so he has to play with the cards he has
            pass

        # Update the number of coins left for each player
        coins_left -= 1
        gladstone_coins_left -= 1

        # Update the maximum number of coins Donald can have
        max_coins = max(max_coins, coins_left + gladstone_coins_left)

    return max_coins

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    d, g, n, k = map(int, input().split())
    print(f1(d, g, n, k))

