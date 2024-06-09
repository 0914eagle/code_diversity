
def is_fair_game(words):
    if len(words) < 2:
        return "Fair Game"
    prev_word = words[0]
    for i in range(1, len(words)):
        curr_word = words[i]
        if not curr_word.startswith(prev_word[-1]):
            return "Player " + str(i % 2 + 1) + " lost"
        prev_word = curr_word
    return "Fair Game"

