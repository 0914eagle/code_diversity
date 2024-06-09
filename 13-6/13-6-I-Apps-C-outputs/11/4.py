
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

def make_valid_bracket_sequence(bracket_sequence):
    if is_valid_bracket_sequence(bracket_sequence):
        return "possible"
    
    # Find the first unmatched bracket
    for i in range(len(bracket_sequence)):
        if bracket_sequence[i] == "(":
            break
    else:
        return "impossible"
    
    # Invert the segment [i, i]
    bracket_sequence = bracket_sequence[:i] + ")" + bracket_sequence[i+1:]
    return "possible" if is_valid_bracket_sequence(bracket_sequence) else "impossible"

