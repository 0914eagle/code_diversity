
def is_nested(string: str) -> bool:
    
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            stack.pop()
    return not stack

