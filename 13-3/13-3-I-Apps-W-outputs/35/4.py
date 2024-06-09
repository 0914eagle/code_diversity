
def get_max_sum(cards, operations):
    # Initialize the maximum sum to 0
    max_sum = 0
    
    # Loop through each operation
    for operation in operations:
        # Get the number of cards to choose and the value to replace them with
        num_cards, value = operation
        
        # Initialize a list to store the indices of the chosen cards
        chosen_cards = []
        
        # Loop through each card
        for i in range(len(cards)):
            # If the card has not been chosen and the number of chosen cards is less than the number of cards to choose,
            if i not in chosen_cards and len(chosen_cards) < num_cards:
                # Add the card to the list of chosen cards
                chosen_cards.append(i)
        
        # Loop through each chosen card
        for i in chosen_cards:
            # Replace the value on the card with the given value
            cards[i] = value
    
    # Return the maximum sum of the cards
    return max(cards)

