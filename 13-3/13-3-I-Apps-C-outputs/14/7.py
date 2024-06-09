
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
            break
        # Otherwise, choose a card from Jiro's hand to attack
        else:
            # Find the strongest card in Jiro's hand that is not already dead
            strongest_card = -1
            for jiro_card in Jiro_cards:
                if jiro_card[1] > strongest_card and jiro_card[0] not in Ciel_cards_used:
                    strongest_card = jiro_card[1]
            # If there is no such card, attack with the current card
            if strongest_card == -1:
                Jiro_damage += card
                break
            # Otherwise, attack with the strongest card and update the variables
            else:
                Ciel_damage += card - strongest_card
                Jiro_damage += strongest_card
                Ciel_cards_used.append(jiro_card[0])
                Jiro_cards.remove(jiro_card)
                if len(Jiro_cards) == 0:
                    Jiro_alive = False

    # Return the total damage Jiro can get
    return Jiro_damage

def f2(...):
    # Implement function 2 here
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
        Ciel_cards.append(strength)
    print(f1(n, m, Jiro_cards, Ciel_cards))

