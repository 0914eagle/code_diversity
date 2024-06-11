def encode(message):
    
    vowels = 'aeiou'
    vowels_dict = {
        'a': 'c',
        'e': 'g',
        'i': 'i',
        'o': 'k',
        'u': 'm',
    }
    encoded_message = ''
    for letter in message:
        if letter.lower() in vowels:
            encoded_message += vowels_dict[letter.lower()]
        else:
            encoded_message += letter.lower() if letter.isupper() else letter.upper()
    return encoded_message

