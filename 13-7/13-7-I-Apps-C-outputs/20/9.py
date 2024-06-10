
def get_max_damage(jiro_cards, ciel_cards):
    # Initialize variables
    max_damage = 0
    current_damage = 0
    jiro_alive_cards = jiro_cards[:]
    ciel_alive_cards = ciel_cards[:]

    # Loop through each ciel card
    for ciel_card in ciel_alive_cards:
        # If jiro has no alive cards, add ciel card's strength to the total damage
        if not jiro_alive_cards:
            max_damage += ciel_card["strength"]
            continue

        # Find the strongest jiro card that is still alive
        strongest_jiro_card = None
        for jiro_card in jiro_alive_cards:
            if strongest_jiro_card is None or jiro_card["strength"] > strongest_jiro_card["strength"]:
                strongest_jiro_card = jiro_card

        # If the ciel card's strength is greater than or equal to the strongest jiro card's strength, add the difference to the total damage
        if ciel_card["strength"] >= strongest_jiro_card["strength"]:
            max_damage += ciel_card["strength"] - strongest_jiro_card["strength"]
            jiro_alive_cards.remove(strongest_jiro_card)

        # If the ciel card's strength is less than the strongest jiro card's strength, add the ciel card's strength to the total damage
        else:
            max_damage += ciel_card["strength"]

    return max_damage

def main():
    jiro_cards = []
    ciel_cards = []

    # Read the input
    n, m = map(int, input().split())
    for _ in range(n):
        position, strength = input().split()
        jiro_cards.append({"position": position, "strength": int(strength)})
    for _ in range(m):
        strength = int(input())
        ciel_cards.append({"strength": strength})

    # Calculate the maximum damage
    max_damage = get_max_damage(jiro_cards, ciel_cards)

    # Print the result
    print(max_damage)

if __name__ == '__main__':
    main()

