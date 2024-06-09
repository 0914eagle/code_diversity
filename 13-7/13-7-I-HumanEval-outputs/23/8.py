
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
    
    vowels_map = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'm',
        'u': 's'
    }
    
    for vowel in vowels:
        encoded_message = encoded_message.replace(vowel, vowels_map[vowel])
    
    return encoded_message

