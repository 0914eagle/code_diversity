
def is_valid_bracket_sequence(bracket_sequence):
    stack = []
    for bracket in bracket_sequence:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def is_invertible(bracket_sequence):
    stack = []
    for bracket in bracket_sequence:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def invert_segment(bracket_sequence, l, r):
    inverted_sequence = ""
    for i, bracket in enumerate(bracket_sequence, 1):
        if i >= l and i <= r:
            if bracket == "(":
                inverted_sequence += ")"
            else:
                inverted_sequence += "("
        else:
            inverted_sequence += bracket
    return inverted_sequence

def solve(bracket_sequence):
    if is_valid_bracket_sequence(bracket_sequence):
        return "possible"
    if is_invertible(bracket_sequence):
        return "possible"
    return "impossible"

