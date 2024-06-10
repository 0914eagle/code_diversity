
def solve(jiro_cards, ciel_cards):
    # Initialize variables
    jiro_alive_cards = jiro_cards
    ciel_used_cards = []
    damage = 0
    
    # Iterate through each Ciel's card
    for card in ciel_cards:
        # If Jiro has no alive cards, add the damage to the total damage
        if not jiro_alive_cards:
            damage += card["strength"]
        # Otherwise, choose the best card to attack
        else:
            # Find the best card to attack
            best_card = None
            best_card_strength = 0
            for jiro_card in jiro_alive_cards:
                if jiro_card["position"] == "ATK" and jiro_card["strength"] >= card["strength"]:
                    if jiro_card["strength"] > best_card_strength:
                        best_card = jiro_card
                        best_card_strength = jiro_card["strength"]
            # If there is no best card to attack, add the damage to the total damage
            if not best_card:
                damage += card["strength"]
            # Otherwise, attack the best card and update the variables
            else:
                damage += card["strength"] - best_card["strength"]
                jiro_alive_cards.remove(best_card)
                ciel_used_cards.append(card)
    
    # Return the total damage
    return damage

