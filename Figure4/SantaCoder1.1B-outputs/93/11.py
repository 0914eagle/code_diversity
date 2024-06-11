def encode(message):
    
    message = message.upper()
    vowels = 'AEIOU'
    new_message = ''
    for letter in message:
        if letter in vowels:
            new_message += letter.lower()
        else:
            new_message += letter.upper()
    return new_message


