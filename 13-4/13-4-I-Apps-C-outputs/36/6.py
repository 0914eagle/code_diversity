
def solve(n, m, jiro_cards, ciel_cards):
    # Initialize the maximum damage as 0
    max_damage = 0
    
    # Loop through each card in Ciel's hand
    for card in ciel_cards:
        # If the card is an attack card
        if card[0] == "ATK":
            # Loop through each card in Jiro's hand
            for jiro_card in jiro_cards:
                # If the card is an attack card and has a higher strength than the current card
                if jiro_card[0] == "ATK" and jiro_card[1] > card[1]:
                    # Add the difference in strength to the maximum damage
                    max_damage += jiro_card[1] - card[1]
                # If the card is a defense card and has a lower strength than the current card
                elif jiro_card[0] == "DEF" and jiro_card[1] < card[1]:
                    # Add the difference in strength to the maximum damage
                    max_damage += card[1] - jiro_card[1]
    
    # Return the maximum damage
    return max_damage

