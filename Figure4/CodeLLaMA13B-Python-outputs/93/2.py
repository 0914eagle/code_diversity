def encode(message):
    
    encoded = ''
    for letter in message:
        if letter.isupper():
            encoded += letter.lower()
        elif letter.islower():
            encoded += letter.upper()
        else:
            encoded += letter
    return encoded

