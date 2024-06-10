
def is_sequence_possible(oranges, apples):
    if oranges == 0 and apples == 0:
        return "Impossible"
    if oranges == 1 and apples == 1:
        return "AB"
    if oranges == 1 and apples > 1:
        return "A" + is_sequence_possible(0, apples - 1)
    if oranges > 1 and apples == 1:
        return "B" + is_sequence_possible(oranges - 1, 0)
    if oranges > 1 and apples > 1:
        return "AB" + is_sequence_possible(oranges - 1, apples - 1)

def get_sequence(oranges, apples):
    sequence = ""
    while oranges > 0 or apples > 0:
        if oranges == 0:
            sequence += "B"
            apples -= 1
        elif apples == 0:
            sequence += "A"
            oranges -= 1
        else:
            sequence += "AB"
            oranges -= 1
            apples -= 1
    return sequence

def main():
    oranges, apples = map(int, input().split())
    sequence = get_sequence(oranges, apples)
    if sequence == "":
        print("Impossible")
    else:
        print(sequence)

if __name__ == '__main__':
    main()

