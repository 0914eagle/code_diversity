def compare_one(a, b):
    
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b if b > a else None
    elif isinstance(a, float) and isinstance(b, float):
        return a if a > b else b if b > a else None
    elif isinstance(a, str) and isinstance(b, str):
        return a if a > b else b if b > a else None
    else:
        return None


