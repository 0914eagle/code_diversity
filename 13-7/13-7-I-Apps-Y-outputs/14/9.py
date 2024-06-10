
import collections

def get_suits(deck):
    suits = ["P", "K", "H", "T"]
    suit_count = [0] * 4
    for card in deck:
        suit = card[0]
        if suit in suits:
            suit_index = suits.index(suit)
            suit_count[suit_index] += 1
    return suit_count

def get_cards(deck):
    cards = []
    for card in deck:
        cards.append(card[1:])
    return cards

def get_missing_cards(deck):
    cards = get_cards(deck)
    suits = get_suits(deck)
    if len(cards) != 52:
        return "GRESKA"
    for card in cards:
        if cards.count(card) > 1:
            return "GRESKA"
    missing_cards = [52 - suits[i] for i in range(4)]
    return " ".join(str(missing_card) for missing_card in missing_cards)

def main():
    deck = input()
    print(get_missing_cards(deck))

if __name__ == '__main__':
    main()

