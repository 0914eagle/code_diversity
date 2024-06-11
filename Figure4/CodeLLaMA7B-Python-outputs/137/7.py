def compare_one(a, b):
    
    if a == b:
        return None
    elif isinstance(a, str):
        a = a.replace(",", ".")
    elif isinstance(b, str):
        b = b.replace(",", ".")
    return a if a > b else b


