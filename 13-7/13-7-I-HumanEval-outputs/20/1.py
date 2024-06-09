
def is_nested(string: str) -> bool:
    
    if len(string) % 2 != 0:
        return False

    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()

    return not stack

