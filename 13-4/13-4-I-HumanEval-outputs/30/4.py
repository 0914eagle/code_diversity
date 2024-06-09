
def cycpattern_check(a: str, b: str) -> bool:
    
    return b in a or any(b in a[i:] for i in range(len(a)))

