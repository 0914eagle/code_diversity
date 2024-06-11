def correct_bracketing(brackets: str):
    
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                return False
            if stack[-1] != "(":
                return False
            stack.pop()
    return not stack


