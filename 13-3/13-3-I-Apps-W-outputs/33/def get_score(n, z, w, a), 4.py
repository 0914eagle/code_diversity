
def get_score(n, z, w, a):
    # Initialize the score and the number of cards drawn
    score = 0
    num_cards_drawn = 0
    
    # Loop through the cards in the deck
    for i in range(n):
        # If the current card is not the last card in the deck, draw it
        if i < n-1:
            num_cards_drawn += 1
        
        # Update the score based on the current card and the number of cards drawn
        score += abs(a[i] - a[i+num_cards_drawn])
    
    # Return the score
    return score

