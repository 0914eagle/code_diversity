
def encode(message: str) -> str:
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
        elif char in vowels:
            index = vowels.index(char)
            encoded_message += vowels[(index + 2) % len(vowels)]
        else:
            encoded_message += char
    return encoded_message

