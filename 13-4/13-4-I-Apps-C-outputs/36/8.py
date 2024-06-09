
def solve(n, m, jiro_cards, ciel_cards):
    # Initialize the maximum damage as 0
    max_damage = 0
    
    # Loop through each card in Ciel's hand
    for card in ciel_cards:
        # If the card is an attack card
        if card[0] == "ATK":
            # Loop through each card in Jiro's hand
            for jiro_card in jiro_cards:
                # If the card is still alive and the attack card's strength is greater than or equal to the Jiro's card's strength
                if jiro_card[1] > 0 and card[1] >= jiro_card[1]:
                    # Update the maximum damage
                    max_damage += card[1] - jiro_card[1]
                    # Remove the Jiro's card from the list
                    jiro_cards.remove(jiro_card)
                    # Break out of the loop
                    break
    
    # Return the maximum damage
    return max_damage

