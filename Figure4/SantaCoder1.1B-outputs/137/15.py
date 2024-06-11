def compare_one(a, b):
    
    if type(a) is type(b):
        if type(a) is int:
            return max(a, b)
        elif type(a) is float:
            return max(a, b)
        elif type(a) is str:
            return max(a, b)
    return None


