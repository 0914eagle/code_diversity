def correct_bracketing(brackets: str):
    
    if len(brackets) == 0:
        return True
    elif len(brackets) == 1:
        return False
    else:
        if brackets[0] == "(":
            return correct_bracketing(brackets[1:])
        elif brackets[0] == ")":
            return correct_bracketing(brackets[1:])
        else:
            return False


