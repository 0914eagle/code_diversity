
def get_points(N, B, cards):
    # Initialize a dictionary to map each card to its value
    card_values = {
        "A": 11,
        "K": 4,
        "Q": 3,
        "J": 20,
        "T": 10,
        "9": 14,
        "8": 0,
        "7": 0
    }
    
    # Initialize a variable to store the total points
    total_points = 0
    
    # Iterate through each hand
    for i in range(N):
        # Get the suit of the current hand
        suit = cards[i * 4][1]
        
        # If the suit is the dominant suit, get the value of the card
        if suit == B:
            card_value = card_values[cards[i * 4][0]]
        # Otherwise, get the value of the card
        else:
            card_value = card_values[cards[i * 4][0]]
        
        # Add the value of the card to the total points
        total_points += card_value
    
    # Return the total points
    return total_points

