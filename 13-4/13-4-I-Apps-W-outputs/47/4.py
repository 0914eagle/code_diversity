
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

def make_pairs(bracket_sequences):
    pairs = []
    for sequence in bracket_sequences:
        if is_correct_bracket_sequence(sequence):
            pairs.append(sequence)
    return pairs

def main():
    n = int(input())
    bracket_sequences = []
    for _ in range(n):
        bracket_sequences.append(input())
    print(len(make_pairs(bracket_sequences)))

if __name__ == '__main__':
    main()

