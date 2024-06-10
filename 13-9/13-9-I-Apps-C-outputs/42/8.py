
def get_cards(oranges, apples):
    if oranges == 0 and apples == 0:
        return "Impossible"
    if oranges == 0 or apples == 0:
        return "1A" if oranges == 0 else "1B"
    if oranges == 1 and apples == 1:
        return "AB"
    if oranges == 1 and apples > 1:
        return "A" + get_cards(0, apples-1)
    if apples == 1 and oranges > 1:
        return "B" + get_cards(oranges-1, 0)
    if oranges > 1 and apples > 1:
        return "AB" + get_cards(oranges-1, apples-1)

def get_sequence(oranges, apples):
    cards = []
    while oranges > 0 and apples > 0:
        if oranges > apples:
            cards.append("A")
            oranges -= 1
        elif oranges < apples:
            cards.append("B")
            apples -= 1
        else:
            cards.append("AB")
            oranges -= 1
            apples -= 1
    return "".join(cards)

def get_compressed_sequence(oranges, apples):
    sequence = get_sequence(oranges, apples)
    if sequence == "Impossible":
        return sequence
    compressed_sequence = ""
    count = 1
    for i in range(len(sequence)-1):
        if sequence[i] == sequence[i+1]:
            count += 1
        else:
            compressed_sequence += str(count) + sequence[i]
            count = 1
    compressed_sequence += str(count) + sequence[-1]
    return compressed_sequence

if __name__ == '__main__':
    oranges, apples = map(int, input().split())
    print(get_compressed_sequence(oranges, apples))

