
def f1(n, m, Jiro_cards, Ciel_cards):
    # Initialize the maximum damage as 0
    max_damage = 0
    
    # Loop through all possible combinations of Ciel's cards
    for i in range(1 << m):
        # Initialize the current damage as 0
        current_damage = 0
        
        # Loop through all Jiro's cards
        for j in range(n):
            # Check if the current card is alive
            if Jiro_cards[j][1] > 0:
                # Check if the current card is attack or defense
                if Jiro_cards[j][0] == "ATK":
                    # Check if the current card is stronger than the chosen card
                    if Jiro_cards[j][1] > Ciel_cards[i][0]:
                        # Add the difference in strength to the current damage
                        current_damage += Jiro_cards[j][1] - Ciel_cards[i][0]
                        # Set the current card's strength to 0
                        Jiro_cards[j][1] = 0
                else:
                    # Check if the current card is weaker than the chosen card
                    if Jiro_cards[j][1] < Ciel_cards[i][0]:
                        # Set the current card's strength to 0
                        Jiro_cards[j][1] = 0
        
        # Add the current damage to the maximum damage
        max_damage = max(max_damage, current_damage)
    
    # Return the maximum damage
    return max_damage

def f2(...):
    # TODO: Implement this function
    pass

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    Jiro_cards = []
    for i in range(n):
        Jiro_cards.append(input().split())
    Ciel_cards = []
    for i in range(m):
        Ciel_cards.append(int(input()))
    print(f1(n, m, Jiro_cards, Ciel_cards))

