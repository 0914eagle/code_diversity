
def cycpattern_check(a: str, b: str) -> bool:
    
    if b in a:
        return True
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False

