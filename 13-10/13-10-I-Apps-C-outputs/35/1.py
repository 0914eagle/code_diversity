
def get_cards_sequence(oranges, apples):
    cards = []
    while oranges > 0 and apples > 0:
        if oranges > apples:
            cards.append('A')
            oranges -= 1
        else:
            cards.append('B')
            apples -= 1
    return cards

def get_compressed_sequence(cards):
    compressed_cards = []
    count = 1
    for i in range(len(cards)-1):
        if cards[i] == cards[i+1]:
            count += 1
        else:
            compressed_cards.append(str(count))
            compressed_cards.append(cards[i])
            count = 1
    compressed_cards.append(str(count))
    compressed_cards.append(cards[-1])
    return ''.join(compressed_cards)

def main():
    oranges, apples = map(int, input().split())
    cards = get_cards_sequence(oranges, apples)
    if len(cards) == 0:
        print("Impossible")
    else:
        print(get_compressed_sequence(cards))

if __name__ == '__main__':
    main()

