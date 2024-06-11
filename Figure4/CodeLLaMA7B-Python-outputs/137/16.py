def compare_one(a, b):
    
    if a == b:
        return None
    elif type(a) == type(b):
        return max(a, b)
    else:
        return max(a, b)


