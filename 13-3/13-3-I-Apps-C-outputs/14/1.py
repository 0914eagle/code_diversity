
def f1(n, m, Jiro_cards, Ciel_cards):
    # Initialize the maximum damage as 0
    max_damage = 0
    
    # Loop through all possible combinations of Ciel's cards
    for i in range(1 << m):
        # Initialize the current damage as 0
        current_damage = 0
        
        # Loop through all Jiro's cards
        for j in range(n):
            # If Jiro's card is alive
            if Jiro_cards[j] > 0:
                # Find the index of the strongest Ciel's card that can attack Jiro's card
                attack_card = m
                for k in range(m):
                    if i & (1 << k) and Ciel_cards[k] >= Jiro_cards[j]:
                        attack_card = k
                        break
                
                # If there is no Ciel's card that can attack Jiro's card, break the loop
                if attack_card == m:
                    break
                
                # Update the current damage
                current_damage += Ciel_cards[attack_card]
                Jiro_cards[j] -= Ciel_cards[attack_card]
        
        # If Jiro has no alive cards, update the maximum damage
        if j == n - 1:
            max_damage = max(max_damage, current_damage)
    
    return max_damage

def f2(...):
    ...

if __name__ == '__main__':
    n, m = map(int, input().split())
    Jiro_cards = list(map(int, input().split()))
    Ciel_cards = list(map(int, input().split()))
    print(f1(n, m, Jiro_cards, Ciel_cards))

