
import re

def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    card_count = {suit: 0 for suit in suits}
    for card in deck:
        suit, number = card[0], card[2:]
        if suit in card_count and number in numbers:
            card_count[suit] += 1
        else:
            return "GRESKA"
    return " ".join(str(card_count[suit] - 1) for suit in suits)

deck = input()
print(get_missing_cards(deck))

