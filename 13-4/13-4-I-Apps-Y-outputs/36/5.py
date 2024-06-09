
def rock_paper_scissors(rounds, sven_symbols, friends_symbols):
    sven_scores = 0
    largest_possible_score = 0
    for i in range(len(rounds)):
        if sven_symbols[i] == friends_symbols[i]:
            sven_scores += 1
        elif sven_symbols[i] == "S" and friends_symbols[i] == "P":
            sven_scores += 2
        elif sven_symbols[i] == "P" and friends_symbols[i] == "R":
            sven_scores += 2
        elif sven_symbols[i] == "R" and friends_symbols[i] == "S":
            sven_scores += 2
        largest_possible_score += 2
    return sven_scores, largest_possible_score

