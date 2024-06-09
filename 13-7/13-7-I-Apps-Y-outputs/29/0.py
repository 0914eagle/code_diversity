
def shiritori(words):
    if len(words) == 1:
        return "Fair Game"
    else:
        last_word = words[0]
        for i in range(1, len(words)):
            if words[i][0] != last_word[-1]:
                return "Player " + str(i % 2 + 1) + " lost"
            last_word = words[i]
        return "Fair Game"

