
def camel_race(n, jaap_bet, jan_bet, thijs_bet):
    # Initialize a dictionary to store the pairs of camels in the same order
    same_order = {}

    # Iterate through each camel in Jaap's bet
    for i in range(n):
        # Get the camel in the same position in Jan's and Thijs' bets
        j_camel = jan_bet[i]
        t_camel = thijs_bet[i]

        # If the camel in the same position in Jan's and Thijs' bets is also in the same position in Jaap's bet, increment the count for that pair
        if j_camel == t_camel == jaap_bet[i]:
            if (j_camel, t_camel) in same_order:
                same_order[(j_camel, t_camel)] += 1
            else:
                same_order[(j_camel, t_camel)] = 1

    # Return the number of pairs of camels that appear in the same order in all 3 bets
    return len(same_order)

