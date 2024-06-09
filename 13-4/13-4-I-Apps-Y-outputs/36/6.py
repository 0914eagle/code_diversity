
def rock_paper_scissors(rounds, sven_symbols, friends_symbols):
    # Initialize variables to track scores
    sven_score = 0
    largest_possible_score = 0

    # Loop through each round
    for i in range(len(rounds)):
        # Get the symbol shown by Sven in this round
        sven_symbol = sven_symbols[i]

        # Loop through each friend in this round
        for j in range(len(friends_symbols)):
            # Get the symbol shown by the friend in this round
            friend_symbol = friends_symbols[j][i]

            # Check if Sven won this round
            if (sven_symbol == "S" and friend_symbol == "R") or (sven_symbol == "P" and friend_symbol == "S") or (sven_symbol == "R" and friend_symbol == "P"):
                sven_score += 2
            # Check if there was a tie
            elif sven_symbol == friend_symbol:
                sven_score += 1

        # Update the largest possible score
        largest_possible_score = max(largest_possible_score, sven_score)

    # Return the actual score and the largest possible score
    return sven_score, largest_possible_score

