
def is_nested(string: str) -> bool:
    
    stack = []
    for char in string:
        if char == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack

