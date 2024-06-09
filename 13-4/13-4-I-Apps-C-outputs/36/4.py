
def solve(n, m, jiro_cards, ciel_cards):
    # Initialize the maximum damage as 0
    max_damage = 0
    
    # Iterate over each card in Ciel's hand
    for card in ciel_cards:
        # If the card's position is Attack
        if card[0] == "ATK":
            # Iterate over each card in Jiro's hand
            for jiro_card in jiro_cards:
                # If the card's position is Defense
                if jiro_card[0] == "DEF":
                    # Calculate the damage and update the maximum damage
                    damage = card[1] - jiro_card[1]
                    max_damage = max(max_damage, damage)
    
    # Return the maximum damage
    return max_damage
