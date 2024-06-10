
import re

def get_card_suits(deck):
    suits = ["P", "K", "H", "T"]
    suit_count = [0] * 4
    for card in deck:
        suit = card[0]
        if suit in suits:
            suit_count[suits.index(suit)] += 1
    return suit_count

def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    suit_count = get_card_suits(deck)
    missing_cards = []
    for i in range(4):
        missing_cards.append(52 - suit_count[i])
    return missing_cards

def check_duplicates(deck):
    cards = {}
    for card in deck:
        if card in cards:
            return "GRESKA"
        cards[card] = 1
    return "OK"

def main():
    deck = input()
    result = check_duplicates(deck)
    if result == "OK":
        result = get_missing_cards(deck)
    print(" ".join(map(str, result)))

if __name__ == '__main__':
    main()

