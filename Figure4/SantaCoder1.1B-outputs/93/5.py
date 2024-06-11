def encode(message):
    
    # Your code here
    message = message.lower()
    vowels = 'aeiou'
    new_message = ''
    for char in message:
        if char in vowels:
            new_message += chr(ord(char) + 2)
        else:
            new_message += char
    return new_message

