
def cycpattern_check(a: str, b: str) -> bool:
    
    return any(b in a for _ in range(len(a)))

