
def encode(message: str) -> str:
    
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.isupper():
            encoded_message += chr((ord(char) + 26 - ord('A')) % 26 + ord('A'))
        else:
            encoded_message += chr((ord(char) + 26 - ord('a')) % 26 + ord('a'))
        if char in vowels:
            encoded_message += chr((ord(char) + 2) % 26 + ord('a'))
        else:
            encoded_message += char
    return encoded_message

