
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

def solve(bracket_sequence):
    if is_valid_bracket_sequence(bracket_sequence):
        return "possible"
    
    # Invert the segment [3, 3]
    inverted_sequence = bracket_sequence[:3] + "(" + bracket_sequence[4:]
    if is_valid_bracket_sequence(inverted_sequence):
        return "possible"
    
    # Invert the segment [2, 2]
    inverted_sequence = bracket_sequence[:2] + ")" + bracket_sequence[3:]
    if is_valid_bracket_sequence(inverted_sequence):
        return "possible"
    
    return "impossible"

