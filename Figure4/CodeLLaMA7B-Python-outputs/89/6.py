def encrypt(s):
    
    s = s.lower()
    return s.translate(str.maketrans(
        "abc