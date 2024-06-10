
def solve(jiro_cards, ciel_cards):
    # Initialize variables
    jiro_damage = 0
    ciel_cards_copy = ciel_cards.copy()

    # Loop through each Jiro card
    for jiro_card in jiro_cards:
        # If Jiro has no alive cards, add the damage to the total damage
        if not ciel_cards_copy:
            jiro_damage += jiro_card[1]
            continue

        # Find the strongest Ciel card that can attack Jiro's card
        strongest_ciel_card = None
        for ciel_card in ciel_cards_copy:
            if ciel_card[0] == "ATK" and ciel_card[1] >= jiro_card[1]:
                strongest_ciel_card = ciel_card
                break

        # If there is no Ciel card that can attack Jiro's card, add the damage to the total damage
        if not strongest_ciel_card:
            jiro_damage += jiro_card[1]
            continue

        # Remove the Ciel card from the list
        ciel_cards_copy.remove(strongest_ciel_card)

        # If the Ciel card is an attack card, add the difference in strength to the total damage
        if strongest_ciel_card[0] == "ATK":
            jiro_damage += strongest_ciel_card[1] - jiro_card[1]

    return jiro_damage

