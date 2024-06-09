
def is_correct_bracket_sequence(bracket_sequence):
    stack = []
    for bracket in bracket_sequence:
        if bracket == "(":
            stack.append(bracket)
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

def get_maximum_number_of_pairs(pairs):
    maximum_number_of_pairs = 0
    for pair in pairs:
        if pair not in pairs:
            maximum_number_of_pairs += 1
    return maximum_number_of_pairs

def main():
    n = int(input())
    bracket_sequences = []
    for _ in range(n):
        bracket_sequences.append(input())
    correct_bracket_sequences = get_correct_bracket_sequences(bracket_sequences)
    pairs = get_pairs(correct_bracket_sequences)
    maximum_number_of_pairs = get_maximum_number_of_pairs(pairs)
    print(maximum_number_of_pairs)

if __name__ == '__main__':
    main()

