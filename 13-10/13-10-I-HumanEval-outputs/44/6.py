
def correct_bracketing(brackets: str) -> bool:
    
    opening_brackets = ["<"]
    for bracket in brackets:
        if bracket == "<":
            opening_brackets.append(bracket)
        else:
            if not opening_brackets:
                return False
            opening_brackets.pop()
    return not opening_brackets

