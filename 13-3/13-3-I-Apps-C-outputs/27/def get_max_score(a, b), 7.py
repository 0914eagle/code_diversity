
def get_max_score(a, b):
    # Initialize the score and the deck
    score = 0
    deck = []

    # Add "o" cards to the deck
    for i in range(a):
        deck.append("o")

    # Add "x" cards to the deck
    for i in range(b):
        deck.append("x")

    # Iterate through the deck and calculate the score
    for i in range(len(deck)):
        # If the current card is "o", calculate the score for the current block of "o"s
        if deck[i] == "o":
            # Find the length of the current block of "o"s
            block_length = 1
            for j in range(i+1, len(deck)):
                if deck[j] == "o":
                    block_length += 1
                else:
                    break
            # Update the score
            score += block_length ** 2
        # If the current card is "x", calculate the score for the current block of "x"s
        elif deck[i] == "x":
            # Find the length of the current block of "x"s
            block_length = 1
            for j in range(i+1, len(deck)):
                if deck[j] == "x":
                    block_length += 1
                else:
                    break
            # Update the score
            score -= block_length ** 2

    # Return the maximum score and the deck
    return score, "".join(deck)

