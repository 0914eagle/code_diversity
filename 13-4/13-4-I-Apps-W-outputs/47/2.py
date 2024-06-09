
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


def find_pairs(bracket_sequences):
    pairs = []
    for seq in bracket_sequences:
        if is_correct_bracket_sequence(seq):
            pairs.append((seq, ""))
    return pairs


def f1(...):
    ...
    return ...


def f2(...):
    ...
    return ...


if __name__ == '__main__':
    n = int(input())
    bracket_sequences = []
    for _ in range(n):
        bracket_sequences.append(input())
    pairs = find_pairs(bracket_sequences)
    print(len(pairs))

