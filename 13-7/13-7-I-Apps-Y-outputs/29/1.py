
def shiritori(words):
    # Initialize variables
    prev_word = ""
    player = 1

    # Iterate through the list of words
    for word in words:
        # Check if the current word starts with the last letter of the previous word
        if word[0] != prev_word[-1]:
            # If not, return the name of the player who violated the rules
            return f"Player {player} lost"

        # Update the previous word and player
        prev_word = word
        player = (player % 2) + 1

    # If all words are valid, return "Fair Game"
    return "Fair Game"

