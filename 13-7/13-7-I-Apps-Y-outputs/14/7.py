
def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    cards = {}
    for card in deck:
        suit, number = card[0], card[1:]
        if suit not in suits or number not in numbers:
            return "GRESKA"
        cards[card] = True

    missing_cards = 0
    for suit in suits:
        for number in numbers:
            card = suit + number
            if card not in cards:
                missing_cards += 1

    return " ".join(str(missing_cards) for missing_cards in [13, 13, 13, 13] - [missing_cards])

def main():
    deck = input()
    print(get_missing_cards(deck))

if __name__ == '__main__':
    main()

