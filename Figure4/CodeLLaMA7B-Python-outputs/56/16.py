def correct_bracketing(brackets: str):
    
    # Your code here
    stack = []
    for b in brackets:
        if b == '<':
            stack.append(b)
        elif b == '>':
            if stack:
                stack.pop()
            else:
                return False
    return not stack


