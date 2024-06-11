def correct_bracketing(brackets: str):
    
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
    import doctest

    doctest