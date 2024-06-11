def compare_one(a, b):
    
    if a == b:
        return None
    elif type(a) == type(b):
        return max(a, b)
    elif type(a) == int:
        return max(a, float(b))
    elif type(b) == int:
        return max(float(a), b)
    elif type(a) == float:
        return max(a, float(b))
    elif type(b) == float:
        return max(float(a), b)
    elif type(a) == str:
        return max(a, str(b))
    elif type(b) == str:
        return max(str(a), b)


