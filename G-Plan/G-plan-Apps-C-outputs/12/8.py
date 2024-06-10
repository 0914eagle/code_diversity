
def fill_slots(player, deck):
    slots = {'Theta': [set(), set()], 'Friend': [set(), set()]}
    slots_filled = {'Theta': 0, 'Friend': 0}
    discard_pile = set()
    
    for i in range(0, 20, 10):
        for j in range(2):
            slots['Theta' if i == 0 else 'Friend'][j].add(deck[i + j])
    
    current_player = 'Theta'
    idx = 20
    
    while slots_filled['Theta'] < 10 and slots_filled['Friend'] < 10:
        card = deck[idx]
        
        if card in discard_pile or card in slots[current_player][0] or card in slots[current_player][1]:
            discard_pile.add(card)
            current_player = 'Friend' if current_player == 'Theta' else 'Theta'
        else:
            placed = False
            for j in range(2):
                if card == 'J' or card == str(j + 1) or card == 'T':
                    if card == 'J':
                        slot = min([i for i in range(2) if card not in slots[current_player][i]])
                    else:
                        slot = j
                    slots[current_player][slot].add(card)
                    placed = True
                    break
            
            if not placed:
                discard_pile.add(card)
                current_player = 'Friend' if current_player == 'Theta' else 'Theta'
        
        if len(slots[current_player][0]) == 5 and len(slots[current_player][1]) == 5:
            return 'Theta' if current_player == 'Friend' else 'Friend'
        
        slots_filled['Theta'] = len(slots['Theta'][0]) + len(slots['Theta'][1])
        slots_filled['Friend'] = len(slots['Friend'][0]) + len(slots['Friend'][1])
        idx += 1

def main():
    deck = input().strip()
    winner = fill_slots('Theta', deck)
    print('Theta wins' if winner == 'Theta' else 'Theta loses')

if __name__ == "__main__":
    main()
