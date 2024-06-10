
def get_maximum_damage(jiro_cards, ciel_cards):
    # Initialize variables
    total_damage = 0
    jiro_alive_cards = jiro_cards.copy()
    ciel_alive_cards = ciel_cards.copy()

    # Loop through each card in Ciel's hand
    for card in ciel_cards:
        # If Jiro has no alive cards, deal damage equal to the card's strength
        if not jiro_alive_cards:
            total_damage += card["strength"]
            continue

        # Find the strongest Jiro's alive card
        jiro_card = max(jiro_alive_cards, key=lambda x: x["strength"])

        # If the card's position is Attack and its strength is greater than or equal to the Jiro's card's strength, deal damage equal to the card's strength minus the Jiro's card's strength
        if card["position"] == "ATK" and card["strength"] >= jiro_card["strength"]:
            total_damage += card["strength"] - jiro_card["strength"]
            jiro_alive_cards.remove(jiro_card)

        # If the card's position is Defense and its strength is greater than the Jiro's card's strength, deal no damage
        elif card["position"] == "DEF" and card["strength"] > jiro_card["strength"]:
            jiro_alive_cards.remove(jiro_card)

    return total_damage

def main():
    # Read inputs
    n, m = map(int, input().split())
    jiro_cards = []
    ciel_cards = []
    for _ in range(n):
        position, strength = input().split()
        jiro_cards.append({"position": position, "strength": int(strength)})
    for _ in range(m):
        strength = int(input())
        ciel_cards.append({"position": "ATK", "strength": strength})

    # Get the maximum damage
    maximum_damage = get_maximum_damage(jiro_cards, ciel_cards)

    # Print the output
    print(maximum_damage)

if __name__ == '__main__':
    main()

