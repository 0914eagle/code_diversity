
def get_max_damage(jiro_cards, ciel_cards):
    # Initialize variables
    max_damage = 0
    current_damage = 0
    jiro_alive_cards = jiro_cards.copy()
    ciel_alive_cards = ciel_cards.copy()

    # Loop through each ciel card
    for ciel_card in ciel_alive_cards:
        # Check if Jiro has any alive cards
        if len(jiro_alive_cards) == 0:
            # If not, add the damage to the total damage
            max_damage += ciel_card
        else:
            # If Jiro has alive cards, find the strongest Jiro card
            strongest_jiro_card = max(jiro_alive_cards, key=lambda x: x[1])

            # Check if the ciel card is stronger than the strongest Jiro card
            if ciel_card[1] >= strongest_jiro_card[1]:
                # If it is, add the damage to the total damage
                max_damage += ciel_card[1]
                # Remove the Jiro card from the list
                jiro_alive_cards.remove(strongest_jiro_card)
            else:
                # If it's not, add the damage to the current damage
                current_damage += ciel_card[1]

    # Add the current damage to the total damage
    max_damage += current_damage

    return max_damage

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
        ciel_cards.append((strength))

    # Get the maximum damage
    max_damage = get_max_damage(jiro_cards, ciel_cards)

    # Print the result
    print(max_damage)

if __name__ == '__main__':
    main()

