
import re

def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    card_count = {suit: 0 for suit in suits}
    for card in deck:
        match = re.match(r"([PKHT])0?(\d)", card)
        if match:
            suit, number = match.groups()
            card_count[suit] += 1
            if card_count[suit] > 1 and card_count[suit] > card_count["P"]:
                return "GRESKA"
    for suit in suits:
        if card_count[suit] < 13:
            card_count[suit] = 13 - card_count[suit]
    return " ".join(str(card_count[suit]) for suit in suits)

deck = input()
print(get_missing_cards(deck))

