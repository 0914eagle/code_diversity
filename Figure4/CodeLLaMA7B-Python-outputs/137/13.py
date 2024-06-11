def compare_one(a, b):
    
    if a == b:
        return None
    elif type(a) == type(b):
        if type(a) == int:
            return max(a, b)
        elif type(a) == float:
            return max(a, b)
        elif type(a) == str:
            return max(a, b, key=float)
    else:
        return max(a, b, key=type)


