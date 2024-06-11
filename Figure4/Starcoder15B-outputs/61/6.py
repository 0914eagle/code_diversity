def correct_bracketing(brackets: str):
    
    # TODO: implement this function
    if len(brackets) == 0:
        return True
    elif len(brackets) == 1:
        return False
    else:
        if brackets[0] == '(' and brackets[-1] == ')':
            return correct_bracketing(brackets[1:-1])
        else:
            return False


