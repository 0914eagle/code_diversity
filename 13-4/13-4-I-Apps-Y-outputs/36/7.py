
def rock_paper_scissors(rounds, sven_symbols, friends, friend_symbols):
    sven_score = 0
    largest_possible_score = 0
    for i in range(rounds):
        sven_symbol = sven_symbols[i]
        friend_symbols_list = friend_symbols[i]
        for j in range(friends):
            friend_symbol = friend_symbols_list[j]
            if sven_symbol == friend_symbol:
                sven_score += 1
            elif sven_symbol == "S" and friend_symbol == "P":
                largest_possible_score += 2
            elif sven_symbol == "P" and friend_symbol == "R":
                largest_possible_score += 2
            elif sven_symbol == "R" and friend_symbol == "S":
                largest_possible_score += 2
    return sven_score, largest_possible_score

