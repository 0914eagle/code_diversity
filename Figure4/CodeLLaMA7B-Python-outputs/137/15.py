def compare_one(a, b):
    
    if a == b:
        return None
    elif isinstance(a, str):
        a = a.replace(",", ".")
        a = float(a)
    elif isinstance(b, str):
        b = b.replace(",", ".")
        b = float(b)
    if a > b:
        return a
    else:
        return b


