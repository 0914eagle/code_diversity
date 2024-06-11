def compare_one(a, b):
    
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b if b > a else None
    elif isinstance(a, float) and isinstance(b, float):
        return a if a > b else b if b > a else None
    elif isinstance(a, str) and isinstance(b, str):
        a = a.replace(',', '.')
        b = b.replace(',', '.')
        return a if float(a) > float(b) else b if float(b) > float(a) else None
    elif isinstance(a, int) and isinstance(b, float):
        return a if a > b else b if b > a else None
    elif isinstance(a, float) and isinstance(b, int):
        return a if a > b else b if b > a else None
    elif isinstance(a, int) and isinstance(b, str):
        b = b.replace(',', '.')
        return a if a > float(b) else b if float(b) > a else None
    elif isinstance(a, str) and isinstance(b, int):
        a = a.replace(',', '.')
        return a if float(a) > b else b if b > float(a) else None
    elif isinstance(a, float) and isinstance(b, str):
        b = b.replace(',', '.')
        return a if a > float(b) else b if float(b) > a else None
    elif isinstance(a, str) and isinstance(b, float):
        a = a.replace(',', '.')
        return a if float(a) > b else b if b > float(a) else None


