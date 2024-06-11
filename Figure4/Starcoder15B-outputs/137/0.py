def compare_one(a, b):
    
    if type(a) == type(b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif type(a) == int and type(b) == float:
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif type(a) == float and type(b) == int:
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif type(a) == str and type(b) == float:
        if a.replace(",", ".") > b:
            return a
        elif b > a.replace(",", "."):
            return b
        else:
            return None
    elif type(a) == float and type(b) == str:
        if a > b.replace(",", "."):
            return a
        elif b.replace(",", ".") > a:
            return b
        else:
            return None
    elif type(a) == str and type(b) == int:
        if a.replace(",", ".") > b:
            return a
        elif b > a.replace(",", "."):
            return b
        else:
            return None
    elif type(a) == int and type(b) == str:
        if a > b.replace(",", "."):
            return a
        elif b.replace(",", ".") > a:
            return b
        else:
            return None


