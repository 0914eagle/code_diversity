
def rock_paper_scissors(rounds, sven_symbols, friends, friend_symbols):
    # Initialize variables
    sven_score = 0
    largest_possible_score = 0

    # Loop through each round
    for i in range(rounds):
        # Get the symbol shown by Sven in this round
        sven_symbol = sven_symbols[i]

        # Loop through each friend in this round
        for j in range(friends):
            # Get the symbol shown by the friend in this round
            friend_symbol = friend_symbols[j][i]

            # Check if Sven won, tied or lost
            if sven_symbol == "S" and friend_symbol == "P":
                sven_score += 2
            elif sven_symbol == "P" and friend_symbol == "R":
                sven_score += 2
            elif sven_symbol == "R" and friend_symbol == "S":
                sven_score += 2
            elif sven_symbol == friend_symbol:
                sven_score += 1

            # Update the largest possible score
            if sven_symbol == "S" and friend_symbol == "P":
                largest_possible_score += 2
            elif sven_symbol == "P" and friend_symbol == "R":
                largest_possible_score += 2
            elif sven_symbol == "R" and friend_symbol == "S":
                largest_possible_score += 2
            elif sven_symbol == friend_symbol:
                largest_possible_score += 1

    # Return the scores
    return sven_score, largest_possible_score

