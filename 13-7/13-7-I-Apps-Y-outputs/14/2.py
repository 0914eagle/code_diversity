
def get_missing_cards(card_labels):
    suits = ["P", "K", "H", "T"]
    cards_per_suit = [0, 0, 0, 0]
    for label in card_labels:
        suit = label[0]
        number = int(label[1:])
        if suit in suits:
            index = suits.index(suit)
            cards_per_suit[index] += 1
    for i in range(len(suits)):
        if cards_per_suit[i] != 13:
            return "GRESKA"
    return " ".join(str(x) for x in cards_per_suit)

def main():
    card_labels = input()
    print(get_missing_cards(card_labels))

if __name__ == '__main__':
    main()

