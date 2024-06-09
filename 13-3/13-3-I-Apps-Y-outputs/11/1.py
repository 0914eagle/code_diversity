
import collections

def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i).zfill(2) for i in range(1, 14)]
    card_count = collections.Counter(deck)
    missing_cards = []
    for suit in suits:
        for number in numbers:
            card = suit + number
            if card_count[card] == 0:
                missing_cards.append(card)
    if len(missing_cards) == 0:
        return "GRESKA"
    return " ".join(missing_cards)

