def compare_one(a, b):
    
    if type(a) == type(b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    else:
        return None


