
def get_correct_bracket_sequences(n):
    sequences = []
    for i in range(n):
        sequences.append("()")
    for i in range(n):
        for sequence in sequences:
            sequences.append("(" + sequence + ")")
            sequences.append(sequence + "(")
    return sequences

def get_maximum_matching(sequences):
    matching = 0
    for sequence in sequences:
        opening_brackets = 0
        for i in range(len(sequence)):
            if sequence[i] == '(':
                opening_brackets += 1
            else:
                opening_brackets -= 1
            if opening_brackets < 0:
                break
        else:
            matching += 1
    return matching

def main():
    n = int(input())
    sequences = get_correct_bracket_sequences(n)
    print(get_maximum_matching(sequences) % (10**9 + 7))

if __name__ == '__main__':
    main()

