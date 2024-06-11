def correct_bracketing(brackets: str):
    

    if len(brackets) % 2 != 0:
        return False

    count = 0
    for bracket in brackets:
        if bracket == "<":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True


METADATA = {}


