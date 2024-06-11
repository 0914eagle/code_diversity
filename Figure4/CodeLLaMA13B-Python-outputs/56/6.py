def correct_bracketing(brackets: str):
    

    # Hint: Use a stack to keep track of opening brackets.
    # You can push onto the stack whenever you see an opening bracket,
    # and pop from the stack whenever you see a closing bracket.
    # If you try to pop from an empty stack, then the brackets are not correct.
    # If you don't use a stack, then you won't be able to keep track of
    # which closing bracket matches which opening bracket.

    stack = []
    for b in brackets:
        if b == "<":
            stack.append(b)
        elif b == ">":
            if not stack:
                return False
            stack.pop()
    return not stack


