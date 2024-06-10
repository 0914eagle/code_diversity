
def fill_slots(player, deck):
    slots = [[], []]
    for i in range(10):
        slots[player].append(deck[i])
    return slots

def draw_card(deck):
    return deck.pop(0)

def play_game(deck):
    theta = 0
    friend = 1
    slots = fill_slots(theta, deck)
    discard_pile = []
    
    current_player = theta
    while True:
        card = draw_card(deck)
        if card in discard_pile or card in slots[current_player]:
            discard_pile.append(card)
            current_player = 1 - current_player
        else:
            for i, slot in enumerate(slots[current_player]):
                if slot == card or slot == 'J':
                    slots[current_player][i] = card
                    break
            if all(slot != 'J' for slot in slots[current_player]):
                break
    if current_player == theta:
        print("Theta wins")
    else:
        print("Theta loses")

if __name__ == "__main__":
    deck = input().strip()
    play_game(list(deck))
