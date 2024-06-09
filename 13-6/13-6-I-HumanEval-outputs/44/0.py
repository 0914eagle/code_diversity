
def encode(message: str) -> str:
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
            if char in vowels:
                char = chr(ord(char) + 2)
        encoded_message += char
    return encoded_message

