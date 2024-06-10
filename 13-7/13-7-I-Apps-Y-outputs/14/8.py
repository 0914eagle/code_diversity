
def get_card_counts(cards):
    counts = [0, 0, 0, 0]
    for card in cards:
        suit = card[0]
        num = int(card[1:])
        if num == 10:
            num = 1
        counts[suit_to_index[suit]] += 1
    return counts

def get_missing_cards(cards):
    counts = get_card_counts(cards)
    missing = []
    for count in counts:
        if count != 4:
            missing.append(4 - count)
        else:
            missing.append(0)
    return missing

def check_duplicates(cards):
    counts = get_card_counts(cards)
    for count in counts:
        if count > 1:
            return "GRESKA"
    return "OK"

def main():
    cards = input()
    counts = get_missing_cards(cards)
    print(*counts)

if __name__ == '__main__':
    main()

