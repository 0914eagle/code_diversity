
def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    cards = {}
    for card in deck:
        suit = card[0]
        number = card[1:]
        if suit not in cards:
            cards[suit] = set()
        cards[suit].add(number)
    missing_cards = []
    for suit in suits:
        if suit not in cards:
            missing_cards.append(13)
        else:
            missing_cards.append(13 - len(cards[suit]))
    if len(set(missing_cards)) != len(missing_cards):
        return "GRESKA"
    return " ".join(str(card) for card in missing_cards)

def main():
    deck = input()
    print(get_missing_cards(deck))

if __name__ == '__main__':
    main()

