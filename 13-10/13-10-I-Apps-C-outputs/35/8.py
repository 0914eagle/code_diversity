
def get_cards(x, y):
    if x < 1 or y < 1 or x * y < 2:
        return "Impossible"
    cards = []
    while x > 0 and y > 0:
        cards.append("A")
        x -= 1
        y += 1
        cards.append("B")
        x += 1
        y -= 1
    return "".join(cards)

def get_compressed_cards(x, y):
    cards = get_cards(x, y)
    if cards == "Impossible":
        return cards
    compressed_cards = []
    count = 1
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            count += 1
        else:
            compressed_cards.append(str(count))
            compressed_cards.append(cards[i])
            count = 1
    compressed_cards.append(str(count))
    compressed_cards.append(cards[-1])
    return "".join(compressed_cards)

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(get_compressed_cards(x, y))

