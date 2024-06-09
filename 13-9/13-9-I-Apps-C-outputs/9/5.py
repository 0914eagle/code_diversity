
def camel_pairs(n, jaap_bet, jan_bet, thijs_bet):
    # Initialize a dictionary to store the pairs of camels
    pairs = {}

    # Iterate over the bets
    for bet in [jaap_bet, jan_bet, thijs_bet]:
        # Iterate over the pairs of camels in the bet
        for i in range(n - 1):
            for j in range(i + 1, n):
                # If the pair of camels is not in the dictionary, add it
                if (bet[i], bet[j]) not in pairs:
                    pairs[(bet[i], bet[j])] = 1
                # If the pair of camels is already in the dictionary, increment its count
                else:
                    pairs[(bet[i], bet[j])] += 1

    # Return the number of pairs of camels that appear in all 3 bets
    return len([pair for pair, count in pairs.items() if count == 3])

