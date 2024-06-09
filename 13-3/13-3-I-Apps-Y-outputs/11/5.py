
import re

def get_missing_cards(cards):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    missing_cards = [0, 0, 0, 0]
    for suit in suits:
        for number in numbers:
            pattern = suit + "0" + number if len(number) == 1 else suit + number
            if pattern not in cards:
                missing_cards[suits.index(suit)] += 1
    return "GRESKA" if len(set(cards)) != len(cards) else " ".join(str(missing) for missing in missing_cards)

cards = input()
print(get_missing_cards(cards))

