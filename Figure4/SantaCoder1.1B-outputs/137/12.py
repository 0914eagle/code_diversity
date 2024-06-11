def compare_one(a, b):
    
    try:
        if isinstance(a, str):
            a = float(a)
        if isinstance(b, str):
            b = float(b)
        if isinstance(a, float):
            if isinstance(b, float):
                return a if a > b else b
            else:
                return b
        else:
            return a
    except ValueError:
        return None


