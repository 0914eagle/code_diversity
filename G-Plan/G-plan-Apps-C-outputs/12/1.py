
def fill_slots(player, deck):
    slots = [[], []]
    for i in range(10):
        slots[player].append(deck[i])
        slots[1 - player].append(deck[i + 10])
    
    return slots

def simulate_game(deck):
    player = 0
    slots = fill_slots(player, deck)
    discard_pile = []
    
    for card in deck[20:]:
        if card in slots[player]:
            slots[player].remove(card)
        elif card == 'J':
            empty_slots = [i for i, slot in enumerate(slots[player]) if slot == '']
            if empty_slots:
                slots[player][empty_slots[0]] = 'J'
            else:
                discard_pile.append('J')
        else:
            discard_pile.append(card)
        
        if all(slot != '' for slot in slots[player]):
            return "Theta wins"
        
        player = 1 - player
    
    return "Theta loses"

if __name__ == "__main__":
    deck = input().strip()
    result = simulate_game(deck)
    print(result)
