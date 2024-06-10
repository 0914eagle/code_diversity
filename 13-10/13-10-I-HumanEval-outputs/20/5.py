
def cycpattern_check(a: str, b: str) -> bool:
    
    return any(b in a or b in a[1:] or b in a[2:] for i in range(len(a)))

