def encrypt(s):
    
    return ''.join([chr(((ord(i) - 97 + 2) % 26) + 97) for i in s])


