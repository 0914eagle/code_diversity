
def is_rbs(s):
    stack = []
    for char in s:
        if char in ["(", "{", "[", "<"]:
            stack.append(char)
        else:
            if not stack or stack.pop() != match(char):
                return False
    return not stack

def match(char):
    if char == ")":
        return "("
    elif char == "}":
        return "{"
    elif char == "]":
        return "["
    else:
        return "<"

def solve(s):
    if is_rbs(s):
        return 0
    
    # Replace all occurrences of < by {
    s = s.replace("<", "{")
    if is_rbs(s):
        return 1
    
    # Replace all occurrences of > by }
    s = s.replace(">", "}")
    if is_rbs(s):
        return 2
    
    # Replace all occurrences of ) by ]
    s = s.replace(")", "]")
    if is_rbs(s):
        return 3
    
    return -1

