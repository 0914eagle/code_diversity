def correct_bracketing(brackets: str):
    
    # Your code here
    stack = []
    for c in brackets:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


