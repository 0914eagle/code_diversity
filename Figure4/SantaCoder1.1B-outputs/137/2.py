def compare_one(a, b):
    
    if isinstance(a, str):
        a = float(a)
    if isinstance(b, str):
        b = float(b)
    if isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        else:
            return b
    elif isinstance(a, float) and isinstance(b, int):
        return a
    elif isinstance(a, int) and isinstance(b, float):
        return b
    elif isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        else:
            return b
    else:
        return None


