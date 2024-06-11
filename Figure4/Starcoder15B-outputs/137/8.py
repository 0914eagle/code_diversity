def compare_one(a, b):
    
    if a == b:
        return None
    if type(a) == type(b):
        if a > b:
            return a
        else:
            return b
    else:
        if type(a) == int:
            a = float(a)
        elif type(a) == float:
            a = str(a)
        elif type(a) == str:
            a = float(a.replace(",", "."))
        if type(b) == int:
            b = float(b)
        elif type(b) == float:
            b = str(b)
        elif type(b) == str:
            b = float(b.replace(",", "."))
        if a > b:
            return a
        else:
            return b


