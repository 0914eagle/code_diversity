def compare_one(a, b):
    
    if isinstance(a, str):
        a = float(a)
    if isinstance(b, str):
        b = float(b)
    if isinstance(a, float):
        if isinstance(b, float):
            if a > b:
                return a
            else:
                return b
        else:
            return b
    else:
        return a


