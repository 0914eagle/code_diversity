def is_happy(s):
    
    if len(s) < 3:
        return False
    if len(s) % 3 != 0:
        return False
    if s == s[::-1]:
        return True
    return False


