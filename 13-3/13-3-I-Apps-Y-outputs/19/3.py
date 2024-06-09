
def is_fair_game(words):
    if len(words) < 2:
        return "Fair Game"
    
    previous_word = words[0]
    for i in range(1, len(words)):
        current_word = words[i]
        if not current_word.startswith(previous_word[-1]):
            return "Player " + str(i % 2 + 1) + " lost"
        previous_word = current_word
    
    return "Fair Game"

