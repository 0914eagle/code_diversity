
def fill_slots(player, deck):
    slots = [[], []]
    for i in range(10):
        slots[player].append(deck[i])
        slots[1 - player].append(deck[i + 10])
    
    return slots

def play_game(deck):
    player = 0
    slots = fill_slots(player, deck)
    discard_pile = []
    
    for card in deck[20:]:
        if card in slots[player]:
            idx = slots[player].index(card)
            slots[player][idx] = 'filled'
        elif card == 'J':
            unfilled_slots = [i for i, slot in enumerate(slots[player]) if slot != 'filled']
            if unfilled_slots:
                idx = min(unfilled_slots)
                slots[player][idx] = 'filled'
            else:
                discard_pile.append(card)
                player = 1 - player
        else:
            discard_pile.append(card)
            player = 1 - player
        
        if all(slot == 'filled' for slot in slots[player]):
            return 'Theta wins'
    
    return 'Theta loses'

if __name__ == "__main__":
    deck = input().strip()
    result = play_game(deck)
    print(result)
