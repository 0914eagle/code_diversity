def correct_bracketing(brackets: str):
    
    # Your code here
    stack = []
    for b in brackets:
        if b == "<":
            stack.append(b)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
