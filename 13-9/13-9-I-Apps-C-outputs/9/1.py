
def number_of_pairs(n, jaap_bet, jan_bet, thijs_bet):
    # Initialize a dictionary to store the number of pairs for each camel
    camel_pairs = {}

    # Iterate through the bets and count the number of pairs for each camel
    for bet in [jaap_bet, jan_bet, thijs_bet]:
        for i in range(n):
            for j in range(i+1, n):
                if bet[i] == bet[j]:
                    if i + 1 == j:
                        continue
                    camel_pairs[(i+1, j+1)] = camel_pairs.get((i+1, j+1), 0) + 1

    # Return the number of pairs that appear in all 3 bets
    return sum(1 for k, v in camel_pairs.items() if v == 3)

