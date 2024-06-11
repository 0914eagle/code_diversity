def encrypt(s):
    
    s = s.lower()
    return ''.join([chr((ord(i) - 97 + 2) % 26 + 97) for i in s])


