
def solve(s):
    n = len(s)
    if n == 1:
        return "(:("
    
    # Replace ? with (
    s = s.replace("?", "(")
    
    # Check if the resulting sequence is a correct parenthesis sequence
    if is_correct_parenthesis_sequence(s):
        return s
    
    # If not, try replacing ? with )
    s = s.replace("?", ")")
    if is_correct_parenthesis_sequence(s):
        return s
    
    return ":("

def is_correct_parenthesis_sequence(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

