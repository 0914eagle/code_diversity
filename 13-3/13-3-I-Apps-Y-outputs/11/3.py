
import re

def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    missing_cards = [0, 0, 0, 0]
    
    for suit in suits:
        for number in numbers:
            pattern = suit + "0" + number if len(number) == 1 else suit + number
            if pattern not in deck:
                missing_cards[suits.index(suit)] += 1
    
    return missing_cards

def get_duplicate_cards(deck):
    cards = re.findall(r"[A-Z][0-9]", deck)
    return len(cards) != len(set(cards))

deck = input()
if get_duplicate_cards(deck):
    print("GRESKA")
else:
    missing_cards = get_missing_cards(deck)
    print(" ".join(map(str, missing_cards)))

