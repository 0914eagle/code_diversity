
def get_cards_sequence(oranges, apples):
    cards = []
    while oranges > 0 or apples > 0:
        if oranges > apples:
            cards.append('A')
            oranges -= 1
        elif oranges < apples:
            cards.append('B')
            apples -= 1
        else:
            cards.append('A')
            oranges -= 1
            apples -= 1
    return cards

def compress_sequence(cards):
    compressed_cards = []
    count = 1
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            count += 1
        else:
            compressed_cards.append(str(count) + cards[i])
            count = 1
    compressed_cards.append(str(count) + cards[-1])
    return ''.join(compressed_cards)

def get_output(oranges, apples):
    cards = get_cards_sequence(oranges, apples)
    if len(cards) == 0:
        return 'Impossible'
    return compress_sequence(cards)

if __name__ == '__main__':
    oranges, apples = map(int, input().split())
    print(get_output(oranges, apples))

