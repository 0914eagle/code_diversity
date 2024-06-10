
def get_correct_bracket_sequences(n):
    sequences = []
    for i in range(n):
        sequences.append("()")
    for i in range(n):
        for sequence in sequences:
            sequences.append("(" + sequence + ")")
    for i in range(n):
        for sequence1 in sequences:
            for sequence2 in sequences:
                sequences.append(sequence1 + sequence2)
    return sequences

def get_maximum_matching(sequences):
    matching = 0
    for sequence in sequences:
        open_brackets = 0
        for i in range(len(sequence)):
            if sequence[i] == '(':
                open_brackets += 1
            else:
                open_brackets -= 1
            if open_brackets < 0:
                break
        else:
            matching += 1
    return matching

def solve(n):
    sequences = get_correct_bracket_sequences(n)
    return get_maximum_matching(sequences) % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

