
import itertools

def get_hands(deck):
    return deck[:10], deck[10:20]

def get_ace_slot(hand):
    return hand.index(1) + 1

def get_non_ace_slots(hand):
    return [i for i, c in enumerate(hand) if c != 1]

def get_jack_slots(hand):
    return [i for i, c in enumerate(hand) if c == 11]

def get_valid_moves(hand, discarded_cards):
    valid_moves = []
    for i, c in enumerate(hand):
        if c == 0:
            continue
        if c in discarded_cards:
            continue
        if c == 11:
            valid_moves.append(i)
        elif c != 1:
            valid_moves.append(i)
    return valid_moves

def play_game(deck):
    deck = list(deck)
    hands = get_hands(deck)
    discarded_cards = []
    while True:
        for hand in hands:
            valid_moves = get_valid_moves(hand, discarded_cards)
            if not valid_moves:
                return "Theta loses"
            move = valid_moves[0]
            hand[move] = 0
            discarded_cards.append(move + 1)
        hands = get_hands(deck)

def main():
    deck = list(itertools.permutations(range(1, 14)))
    for d in deck:
        result = play_game(d)
        if result == "Theta wins":
            return result
    return result

if __name__ == '__main__':
    print(main())

