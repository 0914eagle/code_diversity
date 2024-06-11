def correct_bracketing(brackets: str):
    
    # Your code here
    stack = []
    for i in brackets:
        if i == '<':
            stack.append(i)
        elif i == '>':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


