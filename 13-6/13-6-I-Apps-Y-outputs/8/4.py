
def get_suits(cards):
    suits = {}
    for card in cards:
        suit = card[0]
        if suit not in suits:
            suits[suit] = 1
        else:
            suits[suit] += 1
    return suits

def get_missing_cards(suits):
    missing_cards = []
    for suit, count in suits.items():
        if count < 13:
            missing_cards.append(13 - count)
        else:
            missing_cards.append(0)
    return missing_cards

def get_error_message(cards):
    cards = set(cards)
    if len(cards) != 52:
        return "GRESKA"
    for card in cards:
        if cards.count(card) > 1:
            return "GRESKA"
    return None

def main():
    cards = input()
    suits = get_suits(cards)
    missing_cards = get_missing_cards(suits)
    error_message = get_error_message(cards)
    if error_message:
        print(error_message)
    else:
        print(" ".join(map(str, missing_cards)))

if __name__ == '__main__':
    main()

