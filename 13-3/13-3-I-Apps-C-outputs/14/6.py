
def f1(n, m, Jiro_cards, Ciel_cards):
    # Initialize variables
    Jiro_alive = True
    Jiro_damage = 0
    Ciel_damage = 0
    Ciel_cards_used = []

    # Loop through each Ciel card
    for card in Ciel_cards:
        # If Jiro is still alive, choose an attack card and attack Jiro
        if Jiro_alive:
            # Choose an attack card with the highest strength
            attack_card = max(Jiro_cards, key=lambda x: x[1])

            # If the attack card's strength is greater than or equal to the Jiro card's strength, attack Jiro and update the damage
            if attack_card[1] >= card:
                Jiro_damage += card
                Jiro_alive = False

        # If Jiro is dead, choose a defense card and attack Jiro
        else:
            # Choose a defense card with the highest strength
            defense_card = max(Jiro_cards, key=lambda x: x[1])

            # If the defense card's strength is greater than the Jiro card's strength, attack Jiro and update the damage
            if defense_card[1] > card:
                Jiro_damage += card

        # Update the Ciel cards used and remove the card from the list
        Ciel_cards_used.append(card)
        Jiro_cards.remove(attack_card)

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

