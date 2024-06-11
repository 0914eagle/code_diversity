def correct_bracketing(brackets: str):
    
    # Your code here
    stack = []
    for c in brackets:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return False
    return not stack


