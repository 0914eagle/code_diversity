def compare_one(a, b):
    
    if type(a) is type(b):
        if type(a) is int:
            return a if a > b else b
        elif type(a) is float:
            return a if a > b else b
        elif type(a) is str:
            return a if a > b else b
        else:
            return None
    else:
        return None


