_slots(player, card, slots):
    for i, slot in enumerate(slots):
        if slot == card:
            slots[i] = None
            return True
    return False

def play_game(deck):
    theta_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    friend_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    discard_pile = []
    current_player = 'Theta'

    for card in deck[20:]:
        if current_player == 'Theta':
            if fill_slots('Theta', card, theta_slots):
                if all(slot is None for slot in theta_slots):
                    print('Theta wins')
                    return
            else:
                discard_pile.append(card)
                current_player = 'Friend'
        else:
            if fill_slots('Friend', card, friend_slots):
                if all(slot is None for slot in friend_slots):
                    print('Theta loses')
                    return
            else:
                discard_pile.append(card)
                current_player = 'Theta'

if __name__ == '__main__':
    deck = input().strip()
    play_game(deck)
""