def compare_one(a, b):
    
    try:
        if isinstance(a, str):
            a = float(a)
        if isinstance(b, str):
            b = float(b)
        if isinstance(a, float) and isinstance(b, float):
            if a > b:
                return a
            elif a < b:
                return b
            else:
                return None
        elif isinstance(a, float) and isinstance(b, int):
            return a
        elif isinstance(a, int) and isinstance(b, float):
            return b
        elif isinstance(a, int) and isinstance(b, int):
            if a > b:
                return a
            elif a < b:
                return b
            else:
                return None
        else:
            return None
    except ValueError:
        return None


