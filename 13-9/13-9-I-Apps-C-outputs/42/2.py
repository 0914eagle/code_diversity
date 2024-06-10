
def get_cards(oranges, apples):
    if oranges == 0 and apples == 0:
        return "Impossible"
    if oranges == 1 and apples == 1:
        return "AB"
    if oranges == 1 and apples > 1:
        return "A" + get_cards(0, apples-1)
    if oranges > 1 and apples == 1:
        return "B" + get_cards(oranges-1, 0)
    if oranges > 1 and apples > 1:
        return "AB" + get_cards(oranges-1, apples-1)

def get_compressed_string(cards):
    compressed_string = ""
    count = 1
    for i in range(len(cards)-1):
        if cards[i] == cards[i+1]:
            count += 1
        else:
            compressed_string += str(count) + cards[i]
            count = 1
    compressed_string += str(count) + cards[len(cards)-1]
    return compressed_string

def main():
    oranges, apples = map(int, input().split())
    cards = get_cards(oranges, apples)
    if cards == "Impossible":
        print(cards)
    else:
        print(get_compressed_string(cards))

if __name__ == '__main__':
    main()

