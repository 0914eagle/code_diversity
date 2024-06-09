
def cycpattern_check(a: str, b: str) -> bool:
    
    return any(b in a for i in range(len(b)))

