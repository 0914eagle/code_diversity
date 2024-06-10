
def calculate_damage(Jiro_cards, Ciel_cards):
    # Initialize variables
    damage = 0
    Jiro_alive_cards = Jiro_cards[:]

    # Iterate through Ciel's cards
    for card in Ciel_cards:
        # If Jiro has no alive cards, attack with current card and calculate damage
        if not Jiro_alive_cards:
            damage += card
            continue

        # Find the strongest Jiro's alive card
        strongest_card = max(Jiro_alive_cards, key=lambda x: x[1])

        # If the current card's strength is greater than the strongest Jiro's alive card's strength, attack with current card and calculate damage
        if card[1] > strongest_card[1]:
            damage += card[1] - strongest_card[1]
            Jiro_alive_cards.remove(strongest_card)

    return damage

def main():
    # Read input
    n, m = map(int, input().split())
    Jiro_cards = [tuple(map(int, input().split())) for _ in range(n)]
    Ciel_cards = [int(input()) for _ in range(m)]

    # Calculate damage
    damage = calculate_damage(Jiro_cards, Ciel_cards)

    # Print output
    print(damage)

if __name__ == '__main__':
    main()

