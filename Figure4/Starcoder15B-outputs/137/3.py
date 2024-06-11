def compare_one(a, b):
    
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif isinstance(a, str) and isinstance(b, str):
        if a.replace(",", ".") > b.replace(",", "."):
            return a
        elif b.replace(",", ".") > a.replace(",", "."):
            return b
        else:
            return None
    else:
        return None


