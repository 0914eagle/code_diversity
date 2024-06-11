def correct_bracketing(brackets: str):
    
    # Your code here
    stack = []
    for i in brackets:
        if i == "<":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
