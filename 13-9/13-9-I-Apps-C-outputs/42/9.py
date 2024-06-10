
def get_cards(x, y):
    if x == 0 and y == 0:
        return "Impossible"
    if x == 0:
        return "B" * y
    if y == 0:
        return "A" * x
    return "A" + get_cards(x-1, y) + "B" + get_cards(x, y-1)

def get_compressed_cards(cards):
    compressed_cards = ""
    count = 1
    for i in range(len(cards)-1):
        if cards[i] == cards[i+1]:
            count += 1
        else:
            compressed_cards += str(count) + cards[i]
            count = 1
    compressed_cards += str(count) + cards[len(cards)-1]
    return compressed_cards

def main():
    x, y = map(int, input().split())
    cards = get_cards(x, y)
    compressed_cards = get_compressed_cards(cards)
    print(compressed_cards)

if __name__ == '__main__':
    main()

