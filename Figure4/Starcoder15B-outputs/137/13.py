def compare_one(a, b):
    
    if a == b:
        return None
    if type(a) == type(b):
        if a > b:
            return a
        else:
            return b
    if type(a) == str:
        a = a.replace(',', '.')
        a = float(a)
    if type(b) == str:
        b = b.replace(',', '.')
        b = float(b)
    if a > b:
        return a
    else:
        return b


