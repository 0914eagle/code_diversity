
def get_max_damage(jiro_cards, ciel_cards):
    # Initialize variables
    max_damage = 0
    jiro_alive_cards = jiro_cards.copy()
    ciel_alive_cards = ciel_cards.copy()

    # Iterate through all possible combinations of cards
    for ciel_card in ciel_alive_cards:
        for jiro_card in jiro_alive_cards:
            # Check if the cards are attack or defense
            if ciel_card[0] == "ATK" and jiro_card[0] == "ATK":
                # Calculate the damage and update the max damage
                damage = ciel_card[1] - jiro_card[1]
                max_damage = max(max_damage, damage)
            elif ciel_card[0] == "ATK" and jiro_card[0] == "DEF":
                # Calculate the damage and update the max damage
                damage = ciel_card[1]
                max_damage = max(max_damage, damage)

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
        ciel_cards.append(strength)

    # Calculate the max damage
    max_damage = get_max_damage(jiro_cards, ciel_cards)

    # Print the result
    print(max_damage)

if __name__ == '__main__':
    main()

