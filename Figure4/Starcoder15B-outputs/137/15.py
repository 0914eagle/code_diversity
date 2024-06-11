def compare_one(a, b):
    
    if a == b:
        return None
    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    if isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    if isinstance(a, str) and isinstance(b, str):
        return max(a, b)
    if isinstance(a, str) and isinstance(b, int):
        return max(a, str(b))
    if isinstance(a, int) and isinstance(b, str):
        return max(str(a), b)
    if isinstance(a, str) and isinstance(b, float):
        return max(a, str(b))
    if isinstance(a, float) and isinstance(b, str):
        return max(str(a), b)


