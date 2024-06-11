def compare_one(a, b):
    
    if type(a) == type(b):
        if type(a) == int:
            return a if a > b else b
        elif type(a) == float:
            return a if a > b else b
        else:
            return a if a > b else b
    else:
        return None


