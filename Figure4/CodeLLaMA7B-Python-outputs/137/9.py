def compare_one(a, b):
    
    if type(a) == type(b):
        if a == b:
            return None
        else:
            return max(a, b)
    else:
        if type(a) == int:
            return max(a, float(b))
        else:
            return max(float(a), b)


