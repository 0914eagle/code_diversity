
def encode(message: str) -> str:
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.isupper():
            if char.lower() in vowels:
                encoded_message += chr((ord(char.lower()) - ord('a') + 2) % 26 + ord('a'))
            else:
                encoded_message += char.lower()
        else:
            if char in vowels:
                encoded_message += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
            else:
                encoded_message += char.upper()
    return encoded_message

