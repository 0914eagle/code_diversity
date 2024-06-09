
def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    card_count = {suit: 0 for suit in suits}
    for card in deck:
        suit, number = card[0], card[2:]
        if suit not in suits or number not in numbers:
            return "GRESKA"
        card_count[suit] += 1
    return " ".join(str(13 - card_count[suit]) for suit in suits)

