
def check_deck(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    missing_cards = [0, 0, 0, 0]
    for card in deck:
        suit = card[0]
        number = card[1:]
        if suit not in suits or number not in numbers:
            return "GRESKA"
        missing_cards[suits.index(suit)] -= 1
    return " ".join(str(x) for x in missing_cards)

def main():
    deck = input()
    print(check_deck(deck))

if __name__ == '__main__':
    main()

