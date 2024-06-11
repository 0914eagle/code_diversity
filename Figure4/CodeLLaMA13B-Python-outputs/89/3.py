def encrypt(s):
    
    return ''.join([chr(ord(c)+2*2) if ord(c) >= ord('a') and ord(c) <= ord('z') else c for c in s])

