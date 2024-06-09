
def is_correct_bracket_sequence(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return not stack


def find_correct_bracket_sequences(bracket_sequences):
    correct_bracket_sequences = []
    for s in bracket_sequences:
        if is_correct_bracket_sequence(s):
            correct_bracket_sequences.append(s)
    return correct_bracket_sequences


def construct_pairs(correct_bracket_sequences):
    pairs = []
    for s in correct_bracket_sequences:
        for t in correct_bracket_sequences:
            if s != t and s + t in correct_bracket_sequences:
                pairs.append((s, t))
    return pairs


def main():
    n = int(input())
    bracket_sequences = []
    for _ in range(n):
        bracket_sequences.append(input())
    correct_bracket_sequences = find_correct_bracket_sequences(bracket_sequences)
    pairs = construct_pairs(correct_bracket_sequences)
    print(len(pairs))


if __name__ == '__main__':
    main()

