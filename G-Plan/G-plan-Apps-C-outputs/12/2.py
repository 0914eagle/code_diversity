_slots(player, deck):
    slots = {'Theta': [set(), set()], 'Friend': [set(), set()]}
    discard_pile = set()
    turn = 'Theta'

    for card in deck[20:]:
        if not any(len(slot) < 5 for slot in slots.values()):
            break

        if card in discard_pile or card in slots[turn][0] or card in slots[turn][1]:
            discard_pile.add(card)
            turn = 'Theta' if turn == 'Friend' else 'Friend'
        else:
            for i, slot in enumerate(slots[turn]):
                if card == 'J' or (i == 0 and card in 'A2345') or (i == 1 and card in '6789T'):
                    slot.add(card)
                    break

    return 'Theta' if all(len(slot) == 5 for slot in slots['Theta']) else 'Friend'

if __name__ == "__main__":
    deck = input().strip()
    winner = fill_slots('Theta', deck)
    print('Theta wins' if winner == 'Theta' else 'Theta loses'