
def is_nested(string: str) -> bool:
    
    if len(string) == 0:
        return False
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

