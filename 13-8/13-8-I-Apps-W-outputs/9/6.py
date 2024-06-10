
def get_correct_bracket_sequences(n):
    sequences = [""]
    for i in range(n):
        new_sequences = []
        for sequence in sequences:
            new_sequences.append("(" + sequence + ")")
            new_sequences.append(sequence + "(")
        sequences = new_sequences
    return sequences

def get_maximum_matching(sequences):
    import itertools
    matching = 0
    for sequence in sequences:
        for i in range(len(sequence)):
            if sequence[i] == "(":
                for j in range(i+1, len(sequence)):
                    if sequence[j] == ")":
                        matching += 1
                        break
    return matching

def main():
    n = int(input())
    sequences = get_correct_bracket_sequences(n)
    matching = get_maximum_matching(sequences)
    print(matching % (10**9 + 7))

if __name__ == '__main__':
    main()

