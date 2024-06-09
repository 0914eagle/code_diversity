
def shiritori(words):
    # Initialize variables
    player = 1
    last_letter = ''

    # Iterate through the words
    for word in words:
        # Check if the word starts with the last letter of the previous word
        if word[0] != last_letter:
            # If the word doesn't start with the last letter, the player has violated the rules
            return "Player " + str(player) + " lost"

        # Update the last letter and player
        last_letter = word[-1]
        player = (player % 2) + 1

    # If the game was played according to the rules, return "Fair Game"
    return "Fair Game"

