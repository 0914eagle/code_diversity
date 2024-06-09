
def is_correct_sequence(sequence):
    stack = []
    for char in sequence:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

def make_sequence_correct(sequence):
    if is_correct_sequence(sequence):
        return 0

    stack = []
    for i in range(len(sequence)):
        char = sequence[i]
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return -1
            stack.pop()
        else:
            continue

    while stack:
        char = stack.pop()
        sequence = sequence[:i] + char + sequence[i:]
        i += 1

    return len(sequence)

