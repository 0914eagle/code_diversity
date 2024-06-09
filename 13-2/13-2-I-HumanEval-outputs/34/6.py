
def encode(message: str) -> str:
    
    vowels = ['a', 'e', 'i', 'o', 'u']
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
            encoded_message = encoded_message[:i] + chr(ord(char) + 2) + encoded_message[i+1:]
    return encoded_message

