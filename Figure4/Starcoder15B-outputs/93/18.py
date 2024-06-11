def encode(message):
    
    vowels = 'aeiou'
    encoded = ''
    for char in message:
        if char.lower() in vowels:
            encoded += chr(ord(char) + 2)
        else:
            encoded += char.swapcase()
    return encoded

