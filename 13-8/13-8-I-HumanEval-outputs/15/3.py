
def cycpattern_check(a: str, b: str) -> bool:
    
    return b in a or b in a[1:] + a[:1] or cycpattern_check(a[1:] + a[:1], b)

