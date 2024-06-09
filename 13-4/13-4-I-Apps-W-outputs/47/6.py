
def is_correct_bracket_sequence(bracket_sequence):
    stack = []
    for char in bracket_sequence:
        if char == "(":
            stack.append(char)
        else:
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return not stack


def get_correct_bracket_sequences(bracket_sequences):
    correct_bracket_sequences = []
    for bracket_sequence in bracket_sequences:
        if is_correct_bracket_sequence(bracket_sequence):
            correct_bracket_sequences.append(bracket_sequence)
    return correct_bracket_sequences


def get_pairs(correct_bracket_sequences):
    pairs = []
    for i in range(len(correct_bracket_sequences)):
        for j in range(i+1, len(correct_bracket_sequences)):
            pair = (correct_bracket_sequences[i], correct_bracket_sequences[j])
            pairs.append(pair)
    return pairs


def get_max_pairs(bracket_sequences):
    correct_bracket_sequences = get_correct_bracket_sequences(bracket_sequences)
    pairs = get_pairs(correct_bracket_sequences)
    return len(pairs)


if __name__ == '__main__':
    n = int(input())
    bracket_sequences = []
    for _ in range(n):
        bracket_sequences.append(input())
    print(get_max_pairs(bracket_sequences))

