def correct_bracketing(brackets: str):
    
    stack = []
    for char in brackets:
        if char == "<":
            stack.append("<")
        elif char == ">":
            if len(stack) == 0:
                return False
            if stack[-1] == ">":
                stack.pop()
            else:
                return False
    return len(stack) == 0


