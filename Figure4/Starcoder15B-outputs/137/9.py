def compare_one(a, b):
    
    if type(a) == type(b):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    else:
        return None


