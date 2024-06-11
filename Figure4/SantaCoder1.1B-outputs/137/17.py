def compare_one(a, b):
    
    try:
        if type(a) == type(b):
            if type(a) == float:
                return a if a > b else b
            elif type(a) == int:
                return a if a > b else b
            elif type(a) == str:
                return a if a > b else b
        else:
            return None
    except TypeError:
        return None


