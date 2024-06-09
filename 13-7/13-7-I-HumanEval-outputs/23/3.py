
def encode(message: str) -> str:
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.isupper():
            if char.lower() in vowels:
                encoded_message += chr((ord(char.lower()) + 2 - 97) % 26 + 65)
            else:
                encoded_message += chr(ord(char) + 32)
        else:
            if char in vowels:
                encoded_message += chr((ord(char) + 2 - 97) % 26 + 97)
            else:
                encoded_message += chr(ord(char) - 32)
    return encoded_message

