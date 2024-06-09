
def shiritori(words):
    if len(words) < 2:
        return "Fair Game"
    else:
        prev_word = words[0]
        for i in range(1, len(words)):
            if not words[i].startswith(prev_word[-1]):
                return "Player " + str(i % 2 + 1) + " lost"
            prev_word = words[i]
        return "Fair Game"

