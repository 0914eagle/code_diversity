
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
            if reply > len(set(suspects)):
                return 0
        else:
            if reply > len(set(suspects)) - 1:
                return 0

    # If the replies are consistent, count the number of admissible solutions
    for i in range(num_suspects):
        for j in range(i+1, num_suspects):
            for k in range(j+1, num_suspects):
                num_solutions += 1

    return num_solutions

