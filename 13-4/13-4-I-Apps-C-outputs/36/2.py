
def solve(n, m, jiro_cards, ciel_cards):
    # Initialize the maximum damage as 0
    max_damage = 0
    
    # Loop through each card in Ciel's hand
    for card in ciel_cards:
        # If the card is an attack card
        if card[0] == "ATK":
            # Loop through each card in Jiro's hand
            for jiro_card in jiro_cards:
                # If the card is still alive
                if jiro_card[1] > 0:
                    # If the card is a defense card
                    if jiro_card[0] == "DEF":
                        # Add the difference between the two card's strength to the maximum damage
                        max_damage += abs(card[1] - jiro_card[1])
                    # If the card is an attack card
                    elif jiro_card[0] == "ATK":
                        # If the attack card's strength is greater than or equal to the defense card's strength
                        if card[1] >= jiro_card[1]:
                            # Add the difference between the two card's strength to the maximum damage
                            max_damage += abs(card[1] - jiro_card[1])
    
    # Return the maximum damage
    return max_damage

