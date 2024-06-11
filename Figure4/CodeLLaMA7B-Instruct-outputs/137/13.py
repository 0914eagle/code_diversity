

def compare_one(a, b):
    
    a_type = type(a)
    b_type = type(b)

    if a_type == b_type:
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif a_type == int and b_type == float:
        return b
    elif a_type == float and b_type == int:
        return a
    elif a_type == str and b_type == str:
        a_float = float(a.replace(",", "."))
        b_float = float(b.replace(",", "."))
        if a_float > b_float:
            return a
        elif b_float > a_float:
            return b
        else:
            return None
    else:
        raise ValueError("Invalid input types")


