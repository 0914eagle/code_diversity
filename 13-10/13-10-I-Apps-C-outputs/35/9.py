
def get_card_sequence(oranges, apples):
    if oranges < 1 or apples < 1:
        return "Impossible"
    
    cards = []
    while oranges > 0 and apples > 0:
        cards.append("A")
        oranges -= 1
        apples -= 1
    
    while oranges > 0 or apples > 0:
        cards.append("B")
        if oranges > 0:
            oranges -= 1
        if apples > 0:
            apples -= 1
    
    return "".join(cards)

def get_compressed_sequence(oranges, apples):
    sequence = get_card_sequence(oranges, apples)
    if sequence == "Impossible":
        return sequence
    
    compressed_sequence = ""
    current_char = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            compressed_sequence += str(count) + current_char
            current_char = sequence[i]
            count = 1
    
    compressed_sequence += str(count) + current_char
    return compressed_sequence

if __name__ == '__main__':
    oranges, apples = map(int, input().split())
    print(get_compressed_sequence(oranges, apples))

