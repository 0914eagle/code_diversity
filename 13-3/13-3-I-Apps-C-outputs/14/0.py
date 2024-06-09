
def f1(n, m, Jiro_cards, Ciel_cards):
    # Initialize variables
    Jiro_alive = True
    Jiro_damage = 0
    Ciel_damage = 0
    Ciel_cards_used = []

    # Loop through each card in Ciel's hand
    for card in Ciel_cards:
        # If Jiro has no alive cards, attack with the current card
        if Jiro_alive == False:
            Jiro_damage += card
            continue

        # Find the strongest Jiro card that is still alive
        strongest_Jiro_card = None
        for jiro_card in Jiro_cards:
            if jiro_card[1] > strongest_Jiro_card[1] and jiro_card[0] == "ATK":
                strongest_Jiro_card = jiro_card

        # If there is no strongest Jiro card, attack with the current card
        if strongest_Jiro_card == None:
            Jiro_damage += card
            continue

        # If the current card is stronger than the strongest Jiro card, attack with the current card
        if card > strongest_Jiro_card[1]:
            Jiro_damage += card - strongest_Jiro_card[1]
            Jiro_cards.remove(strongest_Jiro_card)
            continue

        # If the current card is weaker than the strongest Jiro card, attack with the current card and the strongest Jiro card
        if card < strongest_Jiro_card[1]:
            Jiro_damage += card
            Jiro_cards.remove(strongest_Jiro_card)
            continue

        # If the current card is equal to the strongest Jiro card, attack with the current card and the strongest Jiro card
        if card == strongest_Jiro_card[1]:
            Jiro_damage += card
            Jiro_cards.remove(strongest_Jiro_card)
            continue

    # Return the total damage Jiro can get
    return Jiro_damage

def f2(...):
    # TODO: Implement this function
    pass

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    Jiro_cards = []
    for _ in range(n):
        position, strength = input().split()
        Jiro_cards.append((position, int(strength)))
    Ciel_cards = []
    for _ in range(m):
        strength = int(input())
        Ciel_cards.append(strength)
    print(f1(n, m, Jiro_cards, Ciel_cards))

