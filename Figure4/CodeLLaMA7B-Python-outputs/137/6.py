def compare_one(a, b):
    
    if a == b:
        return None
    elif isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        return max(a, b)
    elif isinstance(a, int) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, int) and isinstance(b, str):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, str):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, float):
        return max(a, b)


