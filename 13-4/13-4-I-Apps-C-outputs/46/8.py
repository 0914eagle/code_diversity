
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
        # If the current card is "o", calculate the score increase
        if deck[i] == "o":
            # Calculate the length of the current block of "o"s
            length = 1
            for j in range(i+1, len(deck)):
                if deck[j] == "o":
                    length += 1
                else:
                    break
            # Update the score
            score += length ** 2
        # If the current card is "x", calculate the score decrease
        elif deck[i] == "x":
            # Calculate the length of the current block of "x"s
            length = 1
            for j in range(i+1, len(deck)):
                if deck[j] == "x":
                    length += 1
                else:
                    break
            # Update the score
            score -= length ** 2
    
    # Return the maximum score and the deck
    return score, "".join(deck)

