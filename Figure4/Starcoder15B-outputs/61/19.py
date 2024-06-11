def correct_bracketing(brackets: str):
    
    return len(brackets) % 2 == 0 and all(
        brackets.count("(") == brackets.count(")")
        for brackets in brackets.split(")")
    )


