
def black_vienna(investigations):
    num_investigations = len(investigations)
    num_suspects = 26
    num_circle = 3
    num_solutions = 0

    for i in range(num_investigations):
        suspects = investigations[i][:2]
        player = investigations[i][2]
        reply = investigations[i][3]

        # Check if the reply is valid
        if reply < 0 or reply > 2:
            return 0

        # Check if the player has the suspects in their hand
        if player == 1:
            if suspects[0] not in player1_hand or suspects[1] not in player1_hand:
                return 0
        elif player == 2:
            if suspects[0] not in player2_hand or suspects[1] not in player2_hand:
                return 0

        # Update the number of solutions
        num_solutions += reply

    # Return the number of solutions
    return num_solutions

