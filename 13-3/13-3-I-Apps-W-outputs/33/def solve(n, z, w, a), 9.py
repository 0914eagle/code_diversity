
def solve(n, z, w, a):
    # Initialize the score and the number of cards drawn
    score = 0
    num_cards_drawn = 0
    
    # Loop through the cards in the deck
    for i in range(n):
        # If X draws a card, add the value to their score and increment the number of cards drawn
        if i % 2 == 0:
            score += a[i]
            num_cards_drawn += 1
        # If Y draws a card, subtract the value from their score and increment the number of cards drawn
        else:
            score -= a[i]
            num_cards_drawn += 1
    
    # Return the score
    return score

