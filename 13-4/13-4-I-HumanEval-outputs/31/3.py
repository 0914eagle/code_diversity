
def encode(message: str) -> str:
    
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.isupper():
            encoded_message += char.lower()
        elif char.islower():
            encoded_message += char.upper()
        else:
            encoded_message += char
    
    for i, char in enumerate(encoded_message):
        if char in vowels:
            index = vowels.index(char)
            encoded_message = encoded_message[:i] + vowels[(index + 2) % 5] + encoded_message[i+1:]
    
    return encoded_message

