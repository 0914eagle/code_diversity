
def fill_slots(player, deck):
    slots = [[], []]
    for i in range(10):
        slots[player].append(deck[i])
        slots[1 - player].append(deck[i + 10])
    
    return slots

def play_game(deck):
    theta = 0
    friend = 1
    slots = fill_slots(theta, deck)
    discard_pile = []
    current_player = theta

    for card in deck[20:]:
        if card in discard_pile or card in slots[current_player]:
            discard_pile.append(card)
        else:
            filled = False
            for i, slot in enumerate(slots[current_player]):
                if slot == card or slot == 'T' or (slot == 'J' and card not in slots[current_player]):
                    slots[current_player][i] = card
                    filled = True
                    break
            if not filled:
                discard_pile.append(card)
        
        if all(len(slot) == 1 for slot in slots[current_player]):
            return "Theta wins" if current_player == theta else "Theta loses"
        
        current_player = 1 - current_player

def main():
    deck = input().strip()
    result = play_game(deck)
    print(result)

if __name__ == "__main__":
    main()
