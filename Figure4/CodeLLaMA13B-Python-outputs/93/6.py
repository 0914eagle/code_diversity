def encode(message):
    
    vowels = 'aeiou'
    vowels_dict = {
        'a': 'c',
        'e': 'g',
        'i': 'i',
        'o': 'k',
        'u': 'm',
        'A': 'C',
        'E': 'G',
        'I': 'I',
        'O': 'K',
        'U': 'M'
    }
    encoded_message = ''
    for letter in message:
        if letter in vowels:
            encoded_message += vowels_dict[letter]
        else:
            encoded_message += letter.upper() if letter.islower() else letter.lower()
    return encoded_message


