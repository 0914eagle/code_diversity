
def is_valid_bracket_sequence(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

def make_valid_bracket_sequence(s):
    if is_valid_bracket_sequence(s):
        return "possible"
    
    # Find the first unmatched bracket
    for i in range(len(s)):
        if s[i] == "(":
            break
    # Invert the segment [i, i+1]
    s = s[:i] + ")" + s[i+1:]
    return "possible" if is_valid_bracket_sequence(s) else "impossible"

