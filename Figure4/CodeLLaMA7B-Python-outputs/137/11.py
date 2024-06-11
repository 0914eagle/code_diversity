def compare_one(a, b):
    
    if a == b:
        return None
    elif isinstance(a, str):
        if a.replace(".", "").replace(",", "").isdigit() and b.replace(".", "").replace(",", "").isdigit():
            return max(a, b, key=float)
        else:
            return max(a, b)
    else:
        return max(a, b, key=float)


