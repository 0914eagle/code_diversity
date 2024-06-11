def correct_bracketing(brackets: str):
    
    if len(brackets) == 0:
        return True
    elif brackets[0] == ")" or brackets[-1] == "(":
        return False
    else:
        return correct_bracketing(brackets[1:-1])

