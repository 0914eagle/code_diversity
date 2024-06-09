
def rock_paper_scissors(rounds, sven_symbols, friends_symbols):
    # Initialize variables to track Sven's score and largest possible score
    score = 0
    largest_possible_score = 0

    # Loop through each round
    for i in range(len(rounds)):
        # Get the symbols for the current round
        sven_symbol = sven_symbols[i]
        friends_symbols_list = friends_symbols[i]

        # Loop through each friend's symbol for the current round
        for friend_symbol in friends_symbols_list:
            # Check if Sven's symbol is the same as the friend's symbol
            if sven_symbol == friend_symbol:
                # If it is, it's a tie and Sven doesn't score any points
                score += 0
            # Check if Sven's symbol beats the friend's symbol
            elif (sven_symbol == "R" and friend_symbol == "S") or (sven_symbol == "P" and friend_symbol == "R") or (sven_symbol == "S" and friend_symbol == "P"):
                # If it does, Sven scores 2 points
                score += 2
            # Check if Sven's symbol loses to the friend's symbol
            elif (sven_symbol == "S" and friend_symbol == "R") or (sven_symbol == "R" and friend_symbol == "P") or (sven_symbol == "P" and friend_symbol == "S"):
                # If it does, Sven scores 1 point
                score += 1

        # Update the largest possible score
        largest_possible_score += 2

    # Return Sven's score and largest possible score
    return score, largest_possible_score

