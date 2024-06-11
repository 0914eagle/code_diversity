def correct_bracketing(brackets: str):
    
    if len(brackets) % 2 != 0:
        return False
    else:
        stack = []
        for bracket in brackets:
            if bracket == "<":
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


if