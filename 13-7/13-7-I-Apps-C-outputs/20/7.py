
def get_max_damage(jiro_cards, ciel_cards):
    # Initialize variables
    max_damage = 0
    jiro_alive_cards = jiro_cards[:]
    ciel_used_cards = []

    # Loop through each ciel card
    for ciel_card in ciel_cards:
        # If Jiro has no alive cards, add the damage to the max damage
        if not jiro_alive_cards:
            max_damage += ciel_card
        # Otherwise, find the appropriate Jiro card to attack
        else:
            # Find the first Jiro card that is alive and has a strength less than or equal to the ciel card's strength
            for jiro_card in jiro_alive_cards:
                if jiro_card[1] <= ciel_card:
                    break
            # If no such card is found, add the damage to the max damage
            if jiro_card[1] > ciel_card:
                max_damage += ciel_card
            # Otherwise, attack the Jiro card and update the variables
            else:
                max_damage += ciel_card - jiro_card[1]
                jiro_alive_cards.remove(jiro_card)
                ciel_used_cards.append(ciel_card)

    # Return the max damage
    return max_damage

def main():
    # Read the input
    n, m = map(int, input().split())
    jiro_cards = []
    for _ in range(n):
        position, strength = input().split()
        jiro_cards.append((position, int(strength)))
    ciel_cards = [int(input()) for _ in range(m)]

    # Get the max damage
    max_damage = get_max_damage(jiro_cards, ciel_cards)

    # Print the result
    print(max_damage)

if __name__ == '__main__':
    main()

