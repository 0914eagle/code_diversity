def compare_one(a, b):
    
    if type(a) is not type(b):
        return None
    if type(a) is int:
        return max(a, b)
    if type(a) is float:
        return max(a, b)
    if type(a) is str:
        return max(a, b)
    return None


