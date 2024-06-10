
def is_complete_deck(cards):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    card_count = {suit: 0 for suit in suits}
    for card in cards:
        suit, number = card[0], card[1:]
        if suit not in suits or number not in numbers:
            return "GRESKA"
        card_count[suit] += 1
    for suit in suits:
        if card_count[suit] != 13:
            return "GRESKA"
    return " ".join([str(13 - card_count[suit]) for suit in suits])

def main():
    cards = input()
    print(is_complete_deck(cards))

if __name__ == '__main__':
    main()

