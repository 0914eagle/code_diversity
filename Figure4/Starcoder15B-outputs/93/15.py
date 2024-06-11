def encode(message):
    
    vowels = 'aeiou'
    new_message = ''
    for char in message:
        if char.lower() in vowels:
            new_message += chr(ord(char) + 2)
        else:
            new_message += char.swapcase()
    return new_message

