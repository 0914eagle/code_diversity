def correct_bracketing(brackets: str):
    
    if len(brackets) % 2 != 0:
        return False
    else:
        return brackets.count("<") == brackets.count(">")


