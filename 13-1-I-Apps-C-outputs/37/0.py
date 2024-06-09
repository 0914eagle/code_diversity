
def max_coins(d, g, n, k):
    # Initialize variables
    max_coins = 0
    distracted_rounds = 0

    # Loop through each round
    for i in range(n):
        # If Gladstone is distracted, Donald can look at his cards and swap them
        if i < k:
            distracted_rounds += 1

        # Calculate the number of coins each player has left
        d_coins = d - (i - distracted_rounds)
        g_coins = g - i

        # If either player has no coins left, break the loop
        if d_coins == 0 or g_coins == 0:
            break

        # Calculate the maximum number of coins each player can bet
        d_bet = min(d_coins, g_coins)
        g_bet = min(d_coins, g_coins)

        # Update the maximum number of coins Donald can have
        max_coins = max(max_coins, d_bet + g_bet)

    return max_coins

