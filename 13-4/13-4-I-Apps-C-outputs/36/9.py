
def solve(jiro_cards, ciel_cards):
    # Initialize the maximum damage as 0
    max_damage = 0
    # Loop through each card in Ciel's hand
    for card in ciel_cards:
        # Check if the card is attack card
        if card[0] == "ATK":
            # Loop through each card in Jiro's hand
            for jiro_card in jiro_cards:
                # Check if the card is alive
                if jiro_card[1] > 0:
                    # Calculate the damage
                    damage = card[1] - jiro_card[1]
                    # Update the maximum damage
                    max_damage = max(max_damage, damage)
                    # Break the loop if the card is destroyed
                    if jiro_card[1] <= 0:
                        break
    return max_damage

