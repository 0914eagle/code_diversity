
def f1(n, m, Jiro_cards, Ciel_cards):
    # Initialize variables
    Jiro_alive = True
    Jiro_damage = 0
    Ciel_damage = 0
    Ciel_cards_used = []

    # Iterate through Ciel's cards
    for card in Ciel_cards:
        # If Jiro has no alive cards, attack with current card
        if Jiro_alive:
            # Find the strongest Jiro's card that is alive
            strongest_Jiro_card = max(Jiro_cards, key=lambda x: x[1])

            # If the current card is stronger than the strongest Jiro's card, attack with current card
            if card[1] > strongest_Jiro_card[1]:
                Jiro_damage += card[1] - strongest_Jiro_card[1]
                Jiro_cards.remove(strongest_Jiro_card)
                Ciel_cards_used.append(card)
                continue

        # If Jiro has alive cards, attack with current card
        Jiro_damage += card[1]
        Ciel_cards_used.append(card)

    # If Jiro has no alive cards, attack with current card
    if not Jiro_alive:
        Jiro_damage += Ciel_cards[-1][1]
        Ciel_cards_used.append(Ciel_cards[-1])

    return Jiro_damage

def f2(n, m, Jiro_cards, Ciel_cards):
    # Initialize variables
    Jiro_alive = True
    Jiro_damage = 0
    Ciel_damage = 0
    Ciel_cards_used = []

    # Iterate through Ciel's cards
    for card in Ciel_cards:
        # If Jiro has no alive cards, attack with current card
        if Jiro_alive:
            # Find the strongest Jiro's card that is alive
            strongest_Jiro_card = max(Jiro_cards, key=lambda x: x[1])

            # If the current card is stronger than the strongest Jiro's card, attack with current card
            if card[1] > strongest_Jiro_card[1]:
                Jiro_damage += card[1] - strongest_Jiro_card[1]
                Jiro_cards.remove(strongest_Jiro_card)
                Ciel_cards_used.append(card)
                continue

        # If Jiro has alive cards, attack with current card
        Jiro_damage += card[1]
        Ciel_cards_used.append(card)

    # If Jiro has no alive cards, attack with current card
    if not Jiro_alive:
        Jiro_damage += Ciel_cards[-1][1]
        Ciel_cards_used.append(Ciel_cards[-1])

    return Jiro_damage

if __name__ == '__main__':
    n, m = map(int, input().split())
    Jiro_cards = []
    Ciel_cards = []

    for _ in range(n):
        position, strength = input().split()
        Jiro_cards.append((position, int(strength)))

    for _ in range(m):
        strength = int(input())
        Ciel_cards.append((strength))

    print(f1(n, m, Jiro_cards, Ciel_cards))
    print(f2(n, m, Jiro_cards, Ciel_cards))

