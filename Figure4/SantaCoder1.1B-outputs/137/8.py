def compare_one(a, b):
    
    if type(a) == type(b):
        if type(a) == int:
            return max(a, b)
        elif type(a) == float:
            return max(a, b)
        elif type(a) == str:
            return max(a, b)
        else:
            return None
    else:
        return None


