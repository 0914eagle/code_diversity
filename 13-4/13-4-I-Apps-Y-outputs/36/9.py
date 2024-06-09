
def rock_paper_scissors(rounds, sven_symbols, friends, friend_symbols):
    sven_score = 0
    largest_possible_score = 0
    for i in range(rounds):
        if sven_symbols[i] == "S" and friend_symbols[0][i] == "P":
            sven_score += 2
        elif sven_symbols[i] == "P" and friend_symbols[0][i] == "R":
            sven_score += 2
        elif sven_symbols[i] == "R" and friend_symbols[0][i] == "S":
            sven_score += 2
        elif sven_symbols[i] == friend_symbols[0][i]:
            sven_score += 1
        largest_possible_score += 2
    return sven_score, largest_possible_score

