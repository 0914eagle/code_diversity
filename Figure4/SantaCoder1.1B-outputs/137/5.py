def compare_one(a, b):
    
    if isinstance(a, str):
        a = float(a)
    if isinstance(b, str):
        b = float(b)
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None


