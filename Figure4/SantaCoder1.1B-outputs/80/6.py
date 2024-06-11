def is_happy(s):
    
    if len(s) < 3:
        return False
    if len(set(s)) != len(s):
        return False
    return True


