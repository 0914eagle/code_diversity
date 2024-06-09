
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
        strongest_Jiro_card = 0
        for jiro_card in Jiro_cards:
            if jiro_card[1] > strongest_Jiro_card and jiro_card[0] == "ATK":
                strongest_Jiro_card = jiro_card[1]

        # If the current card is stronger than the strongest Jiro card, attack with the current card
        if card > strongest_Jiro_card:
            Jiro_damage += card
            continue

        # If the current card is weaker than the strongest Jiro card, attack with the strongest Jiro card
        else:
            Jiro_damage += strongest_Jiro_card
            Jiro_cards.remove(strongest_Jiro_card)
            Ciel_cards_used.append(card)

    # If Jiro has no alive cards, add the damage from the unused cards to the total damage
    if Jiro_alive == False:
        for card in Ciel_cards_used:
            Jiro_damage += card

    return Jiro_damage

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    Jiro_cards = []
    Ciel_cards = []
    for i in range(n):
        position, strength = input().split()
        Jiro_cards.append((position, int(strength)))
    for i in range(m):
        strength = int(input())
        Ciel_cards.append(int(strength))
    print(f1(n, m, Jiro_cards, Ciel_cards))

