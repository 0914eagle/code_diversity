
def check_deck(cards):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    missing_cards = [0, 0, 0, 0]
    for card in cards:
        suit = card[0]
        number = card[1:]
        if suit not in suits or number not in numbers:
            return "GRESKA"
        if missing_cards[suits.index(suit)] > 0:
            return "GRESKA"
        missing_cards[suits.index(suit)] -= 1
    return " ".join(str(missing) for missing in missing_cards)

def main():
    cards = input()
    print(check_deck(cards))

if __name__ == '__main__':
    main()

