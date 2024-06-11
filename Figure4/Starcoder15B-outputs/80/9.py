def is_happy(s):
    
    if len(s) < 3:
        return False
    for i in range(0, len(s), 3):
        if s[i:i+3] == s[i:i+3][::-1]:
            return False
    return True


