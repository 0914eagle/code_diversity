
def black_vienna(investigations):
    num_investigations = len(investigations)
    num_suspects = 26
    num_solutions = 0

    for i in range(num_investigations):
        suspects = investigations[i][:2]
        player = investigations[i][2]
        reply = investigations[i][3]

        # Check if the reply is valid
        if reply < 0 or reply > 2:
            return 0

        # Check if the suspects are valid
        if not (suspects[0] in range(num_suspects) and suspects[1] in range(num_suspects)):
            return 0

        # Check if the player is valid
        if player != 1 and player != 2:
            return 0

        # Check if the reply is consistent with the player's hand
        if player == 1:
            if reply > num_suspects - 2:
                return 0
        elif player == 2:
            if reply > num_suspects - 1:
                return 0

        # Update the number of solutions
        num_solutions += reply

    return num_solutions

