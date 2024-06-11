def compare_one(a, b):
    
    if isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, str) and isinstance(b, str):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    else:
        return None


