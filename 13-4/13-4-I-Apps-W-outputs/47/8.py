
def is_correct_bracket_sequence(sequence):
    stack = []
    for char in sequence:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

def get_correct_bracket_sequences(bracket_sequences):
    return [sequence for sequence in bracket_sequences if is_correct_bracket_sequence(sequence)]

def get_pairs(bracket_sequences):
    pairs = []
    for sequence in bracket_sequences:
        for other_sequence in bracket_sequences:
            if sequence != other_sequence and sequence + other_sequence in bracket_sequences:
                pairs.append((sequence, other_sequence))
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

