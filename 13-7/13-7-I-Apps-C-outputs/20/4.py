
def get_maximal_damage(n, m, jiro_cards, ciel_cards):
    # Initialize the maximal damage to 0
    max_damage = 0
    
    # Loop through each card in Ciel's hand
    for card in ciel_cards:
        # If the card is an attack card
        if card[0] == "ATK":
            # Loop through each card in Jiro's hand
            for jiro_card in jiro_cards:
                # If the Jiro's card is alive
                if jiro_card[1] > 0:
                    # If the Jiro's card is an attack card
                    if jiro_card[0] == "ATK":
                        # If the attack card's strength is greater than or equal to the Jiro's card's strength
                        if card[1] >= jiro_card[1]:
                            # Update the maximal damage
                            max_damage += card[1] - jiro_card[1]
                            # Kill the Jiro's card
                            jiro_card[1] = 0
                            break
                    # If the Jiro's card is a defense card
                    elif jiro_card[0] == "DEF":
                        # If the attack card's strength is greater than the Jiro's card's strength
                        if card[1] > jiro_card[1]:
                            # Update the maximal damage
                            max_damage += card[1] - jiro_card[1]
                            # Kill the Jiro's card
                            jiro_card[1] = 0
                            break
    
    # Return the maximal damage
    return max_damage

def main():
    # Read the number of cards for Jiro and Ciel
    n, m = map(int, input().split())
    
    # Read the cards for Jiro
    jiro_cards = []
    for _ in range(n):
        position, strength = input().split()
        jiro_cards.append([position, int(strength)])
    
    # Read the cards for Ciel
    ciel_cards = []
    for _ in range(m):
        strength = int(input())
        ciel_cards.append(["ATK", strength])
    
    # Get the maximal damage
    max_damage = get_maximal_damage(n, m, jiro_cards, ciel_cards)
    
    # Print the maximal damage
    print(max_damage)

if __name__ == '__main__':
    main()

