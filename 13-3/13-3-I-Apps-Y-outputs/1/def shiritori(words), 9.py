
def shiritori(words):
    if len(words) == 1:
        return "Fair Game"
    else:
        last_letter = words[0][-1]
        for i in range(1, len(words)):
            if words[i][0] != last_letter:
                return "Player " + str(i) + " lost"
            last_letter = words[i][-1]
        return "Fair Game"

