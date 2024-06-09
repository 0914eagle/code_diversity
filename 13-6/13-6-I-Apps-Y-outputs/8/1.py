
def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    cards = {}
    for card in deck:
        suit, number = card[0], card[1:]
        if suit not in cards:
            cards[suit] = set()
        cards[suit].add(number)
    
    missing_cards = []
    for suit in suits:
        if suit not in cards:
            missing_cards.append(13)
        else:
            missing_cards.append(13 - len(cards[suit]))
    
    return missing_cards

def get_error_message(deck):
    suits = ["P", "K", "H", "T"]
    cards = {}
    for card in deck:
        suit, number = card[0], card[1:]
        if suit not in cards:
            cards[suit] = set()
        cards[suit].add(number)
    
    for suit in suits:
        if suit in cards and len(cards[suit]) > 1:
            return "GRESKA"
    
    return None

if __name__ == '__main__':
    deck = input()
    missing_cards = get_missing_cards(deck)
    error_message = get_error_message(deck)
    if error_message:
        print(error_message)
    else:
        print(" ".join(str(card) for card in missing_cards))

