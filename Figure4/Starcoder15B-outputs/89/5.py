def encrypt(s):
    
    # Your code here
    return ''.join([chr(ord(c) + 2) for c in s])

