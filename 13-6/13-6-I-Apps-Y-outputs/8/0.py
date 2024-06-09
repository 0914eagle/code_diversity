
def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    cards_per_suit = 13
    card_count = {suit: 0 for suit in suits}
    for card in deck:
        card_count[card[0]] += 1
    missing_cards = []
    for suit in suits:
        if card_count[suit] < cards_per_suit:
            missing_cards.append(cards_per_suit - card_count[suit])
        elif card_count[suit] > cards_per_suit:
            return "GRESKA"
    return " ".join(str(card) for card in missing_cards)

def main():
    deck = input()
    print(get_missing_cards(deck))

if __name__ == '__main__':
    main()

