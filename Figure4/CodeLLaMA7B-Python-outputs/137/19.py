def compare_one(a, b):
    
    if type(a) == type(b):
        if a == b:
            return None
        else:
            return max(a, b)
    else:
        if type(a) == str:
            a = a.replace(",", ".")
        if type(b) == str:
            b = b.replace(",", ".")
        if float(a) == float(b):
            return None
        else:
            return max(a, b)


