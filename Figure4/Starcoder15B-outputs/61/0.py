def correct_bracketing(brackets: str):
    
    # TODO: write this function
    # Hint: use a stack
    stack = []
    for i in brackets:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

