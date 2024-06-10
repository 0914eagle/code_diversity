
def correct_bracketing(brackets: str) -> bool:
    
    if len(brackets) % 2 != 0:
        return False
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

