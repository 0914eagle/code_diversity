
def correct_bracketing(brackets: str) -> bool:
    
    stack = []
    for char in brackets:
        if char == "<":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

