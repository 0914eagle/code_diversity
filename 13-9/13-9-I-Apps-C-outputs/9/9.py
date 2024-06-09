
def camel_race(n, jaap_bet, jan_bet, thijs_bet):
    # Initialize a dictionary to store the number of pairs of camels that appear in the same order
    pairs = {}

    # Iterate over the bets
    for bet in [jaap_bet, jan_bet, thijs_bet]:
        # Iterate over the pairs of camels in the bet
        for i in range(n - 1):
            for j in range(i + 1, n):
                # If the pair of camels appears in the same order in all bets, increment the count by 1
                if bet[i] < bet[j] and bet[i + 1] < bet[j + 1]:
                    pairs[(i, j)] = pairs.get((i, j), 0) + 1

    # Return the number of pairs of camels that appear in the same order in all bets
    return sum(pairs.values())

