
def get_sequence(oranges, apples):
    if oranges < 0 or apples < 0:
        return "Impossible"
    if oranges == 0 and apples == 0:
        return ""
    if oranges == 1 and apples == 1:
        return "AB"
    if oranges == 1 and apples > 1:
        return "A" + get_sequence(0, apples - 1)
    if oranges > 1 and apples == 1:
        return "B" + get_sequence(oranges - 1, 0)
    if oranges > 1 and apples > 1:
        return "AB" + get_sequence(oranges - 1, apples - 1)

def get_compressed_sequence(sequence):
    result = ""
    count = 1
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            count += 1
        else:
            result += str(count) + sequence[i]
            count = 1
    result += str(count) + sequence[len(sequence) - 1]
    return result

def main():
    oranges, apples = map(int, input().split())
    sequence = get_sequence(oranges, apples)
    if sequence == "Impossible":
        print(sequence)
    else:
        print(get_compressed_sequence(sequence))

if __name__ == '__main__':
    main()

