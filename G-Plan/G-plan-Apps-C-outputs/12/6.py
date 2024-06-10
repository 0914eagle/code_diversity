
def fill_slots(player, card, slots):
    for i, slot in enumerate(slots[player]):
        if slot == card:
            slots[player][i] = ''
            return True
    return False

def play_game(deck):
    slots = [['A', '2', '3', '4', '5'], ['6', '7', '8', '9', 'T']]
    discard_pile = []
    player = 0

    for card in deck[20:]:
        if fill_slots(player, card, slots):
            if all(slot == '' for slot in slots[player]):
                return 'Theta wins'
        elif card == 'J':
            if fill_slots(player, 'A', slots):
                continue
            if fill_slots(player, '6', slots):
                continue
            if fill_slots(player, '7', slots):
                continue
            if fill_slots(player, '8', slots):
                continue
            if fill_slots(player, '9', slots):
                continue
            if fill_slots(player, 'T', slots):
                continue
            if fill_slots(player, '2', slots):
                continue
            if fill_slots(player, '3', slots):
                continue
            if fill_slots(player, '4', slots):
                continue
            if fill_slots(player, '5', slots):
                continue
        else:
            discard_pile.append(card)
            player = 1 - player

    return 'Theta loses'

if __name__ == "__main__":
    deck = input().strip()
    print(play_game(deck))
