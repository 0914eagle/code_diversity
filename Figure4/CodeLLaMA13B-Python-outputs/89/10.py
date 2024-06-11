def encrypt(s):
    
    s = s.lower()
    new_s = ''
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            if ord(i) >= 110:
                new_s += chr(ord(i) + 14)
            else:
                new_s += chr(ord(i) + 2)
        else:
            new_s += i
    return new_s


