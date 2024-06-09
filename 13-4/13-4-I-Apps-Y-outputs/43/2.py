
def belote_points(n, b, cards):
    # Initialize a dictionary to map suit to value
    suit_values = {"S": 1, "H": 2, "D": 3, "C": 4}
    # Initialize a dictionary to map card number to value
    card_values = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
    # Initialize total points to 0
    total_points = 0
    # Iterate through each hand
    for i in range(n):
        # Get the suit of the current hand
        suit = cards[i * 4][1]
        # Get the value of the current hand
        hand_value = 0
        for j in range(4):
            # Get the number and suit of the current card
            number, suit = cards[i * 4 + j]
            # Check if the suit is dominant
            if suit == b:
                hand_value += card_values[number]
            else:
                hand_value += suit_values[suit]
        # Add the value of the current hand to the total points
        total_points += hand_value
    # Return the total points
    return total_points

