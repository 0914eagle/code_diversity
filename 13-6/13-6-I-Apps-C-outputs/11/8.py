
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
    
    # Check if we can make the sequence valid by inverting a segment
    for i in range(len(bracket_sequence)):
        for j in range(i+1, len(bracket_sequence)):
            inverted_sequence = bracket_sequence[:i] + ")" + bracket_sequence[i:j] + "(" + bracket_sequence[j:]
            if is_valid_bracket_sequence(inverted_sequence):
                return "possible"
    
    return "impossible"

