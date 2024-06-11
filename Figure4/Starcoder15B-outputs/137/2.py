def compare_one(a, b):
    
    if a == b:
        return None
    if isinstance(a, str):
        a = a.replace(",", ".")
        a = float(a)
    if isinstance(b, str):
        b = b.replace(",", ".")
        b = float(b)
    if a > b:
        return a
    else:
        return b


