
def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    suit_count = {suit: 0 for suit in suits}
    number_count = {number: 0 for number in numbers}
    for card in deck:
        suit = card[0]
        number = card[1:]
        suit_count[suit] += 1
        number_count[number] += 1
    missing_cards = []
    for suit in suits:
        if suit_count[suit] != 1:
            missing_cards.append(str(13 - suit_count[suit]))
        else:
            missing_cards.append("0")
    if "0000" in "".join(missing_cards):
        return "GRESKA"
    return " ".join(missing_cards)

