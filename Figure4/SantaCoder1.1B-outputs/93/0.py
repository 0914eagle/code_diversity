def encode(message):
    
    # Your code here
    return ''.join(sorted(message.upper(), key=message.upper().find))

