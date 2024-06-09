
def correct_bracketing(brackets: str) -> bool:
    
    opening_brackets = ["<"]
    closing_brackets = [">"]
    for bracket in brackets:
        if bracket in opening_brackets:
            opening_brackets.append(bracket)
        elif bracket in closing_brackets:
            closing_brackets.append(bracket)
        else:
            return False
    return len(opening_brackets) == len(closing_brackets)

