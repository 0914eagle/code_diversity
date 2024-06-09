
def camel_race(n, jaap_bet, jan_bet, thijs_bet):
    # Initialize a dictionary to store the number of camels in each position
    camel_positions = {}
    for i in range(n):
        camel_positions[i+1] = 0

    # Count the number of camels in each position for Jaap's bet
    for camel in jaap_bet:
        camel_positions[camel] += 1

    # Count the number of camels in each position for Jan's and Thijs' bets
    for bet in [jan_bet, thijs_bet]:
        for camel in bet:
            camel_positions[camel] += 1

    # Count the number of pairs of camels that appear in the same order in all 3 bets
    same_order_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if camel_positions[i+1] == camel_positions[j+1]:
                same_order_pairs += 1

    return same_order_pairs

