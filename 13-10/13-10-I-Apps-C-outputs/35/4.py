
def get_cards(x, y):
    if x == 0 or y == 0:
        return "Impossible"
    if x == 1 and y == 1:
        return "AB"
    if x == 1 and y > 1:
        return "A" + get_cards(1, y-1)
    if y == 1 and x > 1:
        return "B" + get_cards(x-1, 1)
    if x > 1 and y > 1:
        return "A" + get_cards(x-1, y) + "B" + get_cards(x, y-1)

def get_compressed_sequence(sequence):
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

def main():
    x, y = map(int, input().split())
    sequence = get_cards(x, y)
    if sequence == "Impossible":
        print(sequence)
    else:
        compressed_sequence = get_compressed_sequence(sequence)
        print(compressed_sequence)

if __name__ == '__main__':
    main()

