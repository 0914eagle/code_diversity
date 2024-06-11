def correct_bracketing(brackets: str):
    
    # Your code here
    stack = []
    for i in brackets:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
