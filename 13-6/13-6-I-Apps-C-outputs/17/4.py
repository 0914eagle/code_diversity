
def f1(d, g, n, k):
    # Initialize variables
    coins_won = 0
    coins_lost = 0
    rounds_played = 0
    rounds_distracted = 0

    # Play the game
    while rounds_played < n:
        # Determine the amount of coins to bet
        if rounds_played < k:
            # Gladstone is distracted, bet all coins
            bet = d
        else:
            # Gladstone is not distracted, bet half of coins
            bet = d // 2

        # Update variables
        coins_won += bet
        coins_lost += g - bet
        rounds_played += 1
        rounds_distracted += 1

        # Check if the game has ended
        if coins_won >= g or coins_lost >= d:
            break

    # Return the maximum amount of coins won
    return max(coins_won, coins_lost)

def f2(...):
    # Implement function 2 here
    pass

if __name__ == '__main__':
    d, g, n, k = map(int, input().split())
    print(f1(d, g, n, k))

