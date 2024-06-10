
def fill_slots(player, card, slots):
    for i, slot in enumerate(slots[player]):
        if slot == card:
            slots[player][i] = None
            return True
    return False

def simulate_game(deck):
    slots = [[['A', '2', '3', '4', '5'], ['6', '7', '8', '9', 'T']], [['A', '2', '3', '4', '5'], ['6', '7', '8', '9', 'T']]]
    discard_pile = []
    current_player = 0

    for card in deck[20:]:
        if fill_slots(current_player, card, slots):
            if all(slot is None for row in slots[current_player] for slot in row):
                print("Theta wins")
                return
        elif card == 'J':
            filled = False
            for i in range(2):
                for j in range(2):
                    if slots[current_player][i][j] is not None:
                        slots[current_player][i][j] = None
                        filled = True
                        break
                if filled:
                    break
            if all(slot is None for row in slots[current_player] for slot in row):
                print("Theta wins")
                return
        else:
            discard_pile.append(card)
            current_player = 1 - current_player

    print("Theta loses")

if __name__ == "__main__":
    deck = input().strip()
    simulate_game(deck)
