
def cycpattern_check(a: str, b: str) -> bool:
    
    if b in a:
        return True
    else:
        return any(b in a[i:] for i in range(len(a)))

