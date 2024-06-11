def encrypt(s):
    
    s = s.lower()
    new_s = ''
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            new_s += chr((ord(i) - 97 + 2 * 26) % 26 + 97)
        else:
            new_s += i
    return new_s

