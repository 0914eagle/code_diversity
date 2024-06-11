def compare_one(a, b):
    
    if type(a) == type(b):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == int and type(b) == float:
        if a > b:
            return a
        else:
            return b
    elif type(a) == float and type(b) == int:
        if a > b:
            return a
        else:
            return b
    elif type(a) == str and type(b) == float:
        if float(a) > b:
            return a
        else:
            return b
    elif type(a) == float and type(b) == str:
        if a > float(b):
            return a
        else:
            return b
    elif type(a) == str and type(b) == int:
        if float(a) > b:
            return a
        else:
            return b
    elif type(a) == int and type(b) == str:
        if a > float(b):
            return a
        else:
            return b


