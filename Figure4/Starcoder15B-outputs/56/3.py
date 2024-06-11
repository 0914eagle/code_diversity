def correct_bracketing(brackets: str):
    
    return not any(brackets.count(b) % 2 for b in "<>")


