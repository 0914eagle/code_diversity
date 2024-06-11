def compare_one(a, b):
    
    if a == b:
        return None
    if type(a) == type(b):
        if type(a) == int:
            return max(a, b)
        if type(a) == float:
            return max(a, b)
        if type(a) == str:
            a = a.replace(",", ".")
            b = b.replace(",", ".")
            return max(float(a), float(b))
    else:
        if type(a) == int:
            return max(a, float(b))
        if type(a) == float:
            return max(a, float(b))
        if type(a) == str:
            a = a.replace(",", ".")
            return max(float(a), float(b))


