
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
    for i in range(len(encoded_message)):
        if encoded_message[i].lower() in vowels:
            index = vowels.index(encoded_message[i].lower()) + 2
            if index > 5:
                index -= 5
            encoded_message = encoded_message[:i] + vowels[index] + encoded_message[i+1:]
    return encoded_message

