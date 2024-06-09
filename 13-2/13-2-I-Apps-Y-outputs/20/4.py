
import re

def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    card_count = {suit: 0 for suit in suits}
    for card in deck:
        suit, number = card[0], card[2:]
        if suit in suits and number in numbers:
            card_count[suit] += 1
    missing_cards = []
    for suit, count in card_count.items():
        if count < 4:
            missing_cards.append(4 - count)
        elif count > 4:
            return "GRESKA"
    return " ".join(str(card) for card in missing_cards)

deck = input()
print(get_missing_cards(deck))

