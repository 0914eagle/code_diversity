
def f1(d, g, n, k):
    # Initialize variables
    coins = [d, g]
    rounds = []
    distracted = [False] * n

    # Play the game
    for i in range(n):
        # Determine the number of coins to bet
        bet = min(coins[0], coins[1], i + 1)

        # Update the coins and rounds
        coins[0] -= bet
        coins[1] -= bet
        rounds.append(bet)

        # Determine if Gladstone is distracted
        if i < k:
            distracted[i] = True

        # Update the coins and rounds if Gladstone is distracted
        if distracted[i]:
            coins[0] += bet
            coins[1] -= bet
            rounds[i] = 0

    # Return the maximum number of coins Donald can have
    return max(coins[0], coins[1])

def f2(d, g, n, k):
    # Initialize variables
    coins = [d, g]
    rounds = []
    distracted = [False] * n

    # Play the game
    for i in range(n):
        # Determine the number of coins to bet
        bet = min(coins[0], coins[1], i + 1)

        # Update the coins and rounds
        coins[0] -= bet
        coins[1] -= bet
        rounds.append(bet)

        # Determine if Gladstone is distracted
        if i < k:
            distracted[i] = True

        # Update the coins and rounds if Gladstone is distracted
        if distracted[i]:
            coins[0] += bet
            coins[1] -= bet
            rounds[i] = 0

    # Return the maximum number of coins Donald can have
    return max(coins[0], coins[1])

if __name__ == '__main__':
    d, g, n, k = map(int, input().split())
    print(f1(d, g, n, k))
    print(f2(d, g, n, k))

