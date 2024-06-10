
def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    cards_per_suit = 13
    cards_in_deck = {}
    for suit in suits:
        cards_in_deck[suit] = 0
    for card in deck:
        suit = card[0]
        number = int(card[1:])
        if suit in cards_in_deck and number <= cards_per_suit:
            cards_in_deck[suit] += 1
    missing_cards = []
    for suit in suits:
        missing_cards.append(cards_per_suit - cards_in_deck[suit])
    return missing_cards

def check_duplicates(deck):
    for i in range(len(deck)):
        for j in range(i+1, len(deck)):
            if deck[i] == deck[j]:
                return "GRESKA"
    return "OK"

if __name__ == '__main__':
    deck = input()
    missing_cards = get_missing_cards(deck)
    print(" ".join(map(str, missing_cards)))
    if check_duplicates(deck) == "GRESKA":
        print("GRESKA")

