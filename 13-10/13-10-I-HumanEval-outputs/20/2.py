
def cycpattern_check(a: str, b: str) -> bool:
    
    # check if b is a substring in a
    if b in a:
        return True
    # check if any rotation of b is a substring in a
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    # if none of the above conditions are met, return False
    return False

