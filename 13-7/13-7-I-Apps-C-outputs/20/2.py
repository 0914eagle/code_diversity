
def get_maximum_damage(jiro_cards, ciel_cards):
    # Initialize variables
    total_damage = 0
    jiro_alive_cards = jiro_cards.copy()
    ciel_alive_cards = ciel_cards.copy()

    # Loop through each ciel card
    for ciel_card in ciel_cards:
        # Check if Jiro has any alive cards
        if len(jiro_alive_cards) == 0:
            # If not, add the damage to the total damage
            total_damage += ciel_card
        else:
            # Find the strongest Jiro card that is alive
            strongest_jiro_card = max(jiro_alive_cards, key=lambda x: x[1])

            # Check if the ciel card is strong enough to destroy the strongest Jiro card
            if ciel_card >= strongest_jiro_card[1]:
                # If it is, remove the strongest Jiro card from the list
                jiro_alive_cards.remove(strongest_jiro_card)

                # Add the damage to the total damage
                total_damage += ciel_card - strongest_jiro_card[1]
            else:
                # If it's not, add the ciel card to the list of alive ciel cards
                ciel_alive_cards.append(ciel_card)

    # Return the total damage
    return total_damage

def main():
    # Read the input
    n, m = map(int, input().split())
    jiro_cards = []
    ciel_cards = []
    for _ in range(n):
        position, strength = input().split()
        jiro_cards.append((position, int(strength)))
    for _ in range(m):
        strength = int(input())
        ciel_cards.append(strength)

    # Calculate the maximum damage
    total_damage = get_maximum_damage(jiro_cards, ciel_cards)

    # Print the result
    print(total_damage)

if __name__ == '__main__':
    main()

