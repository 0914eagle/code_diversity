def encrypt(s):
    
    return ''.join([chr(ord(c) + 2 * 2) if ord(c) + 2 * 2 < 123 else chr(ord(c) + 2 * 2 - 26) for c in s])


