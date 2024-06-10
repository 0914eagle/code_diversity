
import itertools

def get_winning_player(deck):
    deck = list(deck)
    cards = {card: i for i, card in enumerate(deck, 1)}
    hand = [deck.pop() for _ in range(10)]
    friend_hand = [deck.pop() for _ in range(10)]
    slots = [None] * 10
    for card in hand:
        if card in '2345':
            slots[cards[card] - 1] = card
        elif card in '6789TJQKA':
            slots[cards[card] - 1] = card
        elif card == '9':
            slots[cards[card] - 1] = card
        else:
            slots[cards[card] - 1] = card
    for card in friend_hand:
        if card in '2345':
            slots[cards[card] - 1] = card
        elif card in '6789TJQKA':
            slots[cards[card] - 1] = card
        elif card == '9':
            slots[cards[card] - 1] = card
        else:
            slots[cards[card] - 1] = card
    for card in deck:
        if card in '2345':
            slots[cards[card] - 1] = card
        elif card in '6789TJQKA':
            slots[cards[card] - 1] = card
        elif card == '9':
            slots[cards[card] - 1] = card
        else:
            slots[cards[card] - 1] = card
    for slot in slots:
        if slot is None:
            return 'Theta wins'
    return 'Theta loses'

def main():
    deck = input()
    print(get_winning_player(deck))

if __name__ == '__main__':
    main()

