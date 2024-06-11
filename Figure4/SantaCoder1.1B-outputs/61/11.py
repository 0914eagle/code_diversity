def correct_bracketing(brackets: str):
    
    stack = []
    for char in brackets:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            elif stack[-1] != "(":
                return False
            else:
                stack.pop()
    return not stack


