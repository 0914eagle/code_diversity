
def correct_bracketing(brackets: str) -> bool:
    
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

