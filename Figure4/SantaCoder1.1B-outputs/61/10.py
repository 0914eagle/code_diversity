def correct_bracketing(brackets: str):
    
    stack = []
    for char in brackets:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            elif stack[-1] == "(":
                stack.pop()
            else:
                return False
    return len(stack) == 0


