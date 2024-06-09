
def get_suits(card_labels):
    suits = ["P", "K", "H", "T"]
    suit_counts = {suit: 0 for suit in suits}
    for card_label in card_labels:
        suit = card_label[0]
        if suit in suits:
            suit_counts[suit] += 1
    return suit_counts

def get_missing_cards(card_labels):
    suits = ["P", "K", "H", "T"]
    suit_counts = get_suits(card_labels)
    missing_cards = []
    for suit in suits:
        if suit_counts[suit] < 13:
            missing_cards.append(13 - suit_counts[suit])
        else:
            missing_cards.append(0)
    return missing_cards

def check_duplicates(card_labels):
    suits = ["P", "K", "H", "T"]
    suit_counts = get_suits(card_labels)
    for suit in suits:
        if suit_counts[suit] > 1:
            return "GRESKA"
    return "OK"

def main():
    card_labels = input()
    missing_cards = get_missing_cards(card_labels)
    duplicates = check_duplicates(card_labels)
    if duplicates == "GRESKA":
        print(duplicates)
    else:
        print(" ".join(str(missing_card) for missing_card in missing_cards))

if __name__ == '__main__':
    main()

