
def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    cards_per_suit = 13
    card_count = {suit: 0 for suit in suits}
    for card in deck:
        suit, number = card[0], card[2:]
        if suit in card_count and int(number) <= cards_per_suit:
            card_count[suit] += 1
    return [cards_per_suit - card_count[suit] for suit in suits]

def main():
    deck = input()
    if len(deck) != 52:
        print("GRESKA")
    else:
        print(*get_missing_cards(deck))

if __name__ == '__main__':
    main()

