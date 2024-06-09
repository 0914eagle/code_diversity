
def black_vienna(investigations):
    num_investigations = len(investigations)
    num_suspects = 26
    num_solutions = 0

    for i in range(num_investigations):
        suspects = investigations[i][:2]
        player = investigations[i][2]
        reply = investigations[i][3]

        # If the player has all the cards, there is only one solution
        if reply == num_suspects:
            num_solutions += 1
            continue

        # If the player has no cards, there are no solutions
        if reply == 0:
            return 0

        # If the player has some cards, we need to count the number of solutions
        num_solutions += count_solutions(suspects, player, reply, num_suspects)

    return num_solutions

def count_solutions(suspects, player, reply, num_suspects):
    num_solutions = 0

    # If the player has only one card, there is only one solution
    if reply == 1:
        return 1

    # If the player has two cards, we need to count the number of solutions
    for i in range(num_suspects):
        for j in range(i+1, num_suspects):
            if i != j and i not in suspects and j not in suspects:
                num_solutions += 1

    return num_solutions

