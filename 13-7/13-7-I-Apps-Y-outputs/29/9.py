
def shiritori(words):
    if len(words) == 1:
        return "Fair Game"
    else:
        previous_word = words[0]
        for i in range(1, len(words)):
            current_word = words[i]
            if current_word[0] != previous_word[-1]:
                return "Player " + str(i % 2 + 1) + " lost"
            previous_word = current_word
        return "Fair Game"

